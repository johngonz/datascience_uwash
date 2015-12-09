## Commands for Machine Learning Assignment

setwd('C:/Users/johngonz/datasci_course_materials/assignment5')

# Step 1
data<-read.csv("seaflow_21min.csv")
head(data)
print(summary(data$"pop"))

# Step 2
train_rows<-sample(nrow(data), size = floor(nrow(data)/2))
test_rows<-setdiff(1:nrow(data), train_rows)
training_data<-data[train_rows,]
test_data<-data[test_rows,]

# Step 3
library(ggplot2)
print(qplot(x=data$"pe", y=data$"chl_small", colour = data$"pop"))

# Step 4
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=training_data)
print(model)

# Step 5 
prediction_rpart<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_rpart == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)

# Step 6
library("randomForest")
model <- randomForest(fol, data=training_data)
print(model)
prediction_rf<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_rf == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)
print('importance table')
print(importance(model))

# Step 7
library("e1071")
model <- svm(fol, data=training_data)
print(model)
prediction_svm<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_svm == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)

# Step 8.1
confusionmatrix_rpart<-table(pred = prediction_rpart, true = test_data$pop)
confusionmatrix_rf<-table(pred = prediction_rf, true = test_data$pop)
confusionmatrix_svm<-table(pred = prediction_svm, true = test_data$pop)
print('confusion matrix for decision tree algorithm')
print(confusionmatrix_rpart)
print('confusion matrix for random forest algorithm')
print(confusionmatrix_rf)
print('confusion matrix for support vector machine algorithm')
print(confusionmatrix_svm)

# Step 8.2  
print(qplot(x=data$"time", y=data$"fsc_small", colour = data$"pop"))
print(qplot(x=data$"time", y=data$"fsc_perp", colour = data$"pop"))
print(qplot(x=data$"time", y=data$"fsc_big", colour = data$"pop"))  #This appears to be a non-discrete field
print(qplot(x=data$"time", y=data$"pe", colour = data$"pop"))
print(qplot(x=data$"time", y=data$"chl_small", colour = data$"pop"))
print(qplot(x=data$"time", y=data$"chl_big", colour = data$"pop"))

# Step 8.3  
print(qplot(x=data$"time", y=data$"chl_big", colour = data$"file_id"))
filtered_data<-subset(data,data$"file_id" != 208)

# Step 2 repeated for filtered_data
train_rows<-sample(nrow(filtered_data), size = floor(nrow(filtered_data)/2))
test_rows<-setdiff(1:nrow(filtered_data), train_rows)
training_data<-data[train_rows,]
test_data<-filtered_data[test_rows,]

# Step 3 repeated for filtered_data
library(ggplot2)
print(qplot(x=filtered_data$"pe", y=filtered_data$"chl_small", colour = filtered_data$"pop"))

# Step 4 repeated for filtered_data
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=training_data)
print(model)

# Step 5 repeated for filtered_data
prediction_rpart<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_rpart == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)

# Step 6 repeated for filtered_data
library("randomForest")
model <- randomForest(fol, data=training_data)
print(model)
prediction_rf<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_rf == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)
print('importance table')
print(importance(model))

# Step 7 repeated for filtered_data
library("e1071")
model <- svm(fol, data=training_data)
print(model)
prediction_svm<-predict(model, test_data, type="class")
ground_truth<- test_data$pop
validity<-prediction_svm == ground_truth
proportion_valid <- sum(validity)/length(validity)
print('proportion valid')
print(proportion_valid)

# Step 8.1 repeated for filtered_data
confusionmatrix_rpart<-table(pred = prediction_rpart, true = test_data$pop)
confusionmatrix_rf<-table(pred = prediction_rf, true = test_data$pop)
confusionmatrix_svm<-table(pred = prediction_svm, true = test_data$pop)
print('confusion matrix for decision tree algorithm')
print(confusionmatrix_rpart)
print('confusion matrix for random forest algorithm')
print(confusionmatrix_rf)
print('confusion matrix for support vector machine algorithm')
print(confusionmatrix_svm)

# Step 8.2 repeated for filtered_data
print(qplot(x=filtered_data$"time", y=filtered_data$"fsc_small", colour = filtered_data$"pop"))
print(qplot(x=filtered_data$"time", y=filtered_data$"fsc_perp", colour = filtered_data$"pop"))
print(qplot(x=filtered_data$"time", y=filtered_data$"fsc_big", colour = filtered_data$"pop"))  #This appears to be a non-discrete field
print(qplot(x=filtered_data$"time", y=filtered_data$"pe", colour = filtered_data$"pop"))
print(qplot(x=filtered_data$"time", y=filtered_data$"chl_small", colour = filtered_data$"pop"))
print(qplot(x=filtered_data$"time", y=filtered_data$"chl_big", colour = filtered_data$"pop"))