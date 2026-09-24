# **Waste Material Segregation for Improving Waste Management**

## **Objective**
The objective of this project is to implement an effective waste material segregation system using convolutional neural networks (CNNs) that categorises waste into distinct groups. This process enhances recycling efficiency, minimises environmental pollution, and promotes sustainable waste management practices.

The key goals are:

* Accurately classify waste materials into categories like cardboard, glass, paper, and plastic.
* Improve waste segregation efficiency to support recycling and reduce landfill waste.
* Understand the properties of different waste materials to optimise sorting methods for sustainability.

  ## **Data Understanding**

The Dataset consists of images of some common waste materials.

1. Food Waste
2. Metal
3. Paper
4. Plastic
5. Other
6. Cardboard
7. Glass

**Data Description**

* The dataset consists of multiple folders, each representing a specific class, such as `Cardboard`, `Food_Waste`, and `Metal`.
* Within each folder, there are images of objects that belong to that category.
* However, these items are not further subcategorised. <br> For instance, the `Food_Waste` folder may contain images of items like coffee grounds, teabags, and fruit peels, without explicitly stating that they are actually coffee grounds or teabags.


## Findings about the data

#### Dataset Composition:
 - The dataset consits of images from 7 different categories, namely `Cardboard`, `Food_Waste`, `Glass`, `Metal`, `Paper`,   `Plastic` and `Other`.
 - Each class is represented by a folder containing images of Objects belonging to each category.

### Class Distribution:
 - The dataset has an imbalanced distribution of images across the classes as observed from the bar plot of class distribution.
 - `Plastic` has siginificantly more images(2295) than other categories, `Cardboard` has very low images(540).
 - This might affect model performance.

### Image Characterristics:
 - Images in data set are prest in `.png` format.
 - Resize operation was performed to standardize all images to 128x128 pixels size.

### Label Encoding:
 - Lables were extracted from folder names and encoded into numerical values.
 - One-hot encoding was applied to prepare the labels for model traning.

### Data Splitting:
 - Dataset was split into training & validation sets using 80:20, ensuring the stratification to maintain class distribution in both sets.

### Potential Issues:
 - Dataset contains class imbalance, which may require techniques like data augumentation or class weighting to improve model performance.
 - Some images have overlapping feature between classes, making classification more chaleenging.

## Report model training results

#### Model Architecture:
 - Model consists of 3 convolutional layes with ReLU activation, followed by batch normalization and max-pooling layers.
 - Dropout layers were added to prevent overfitting.
 - Fully connected layers were used for classification, with final layer using a softmax activation for multi-class classification.

 #### Training Process:
 - Model was trained using ADAM Optimizer and Categorical Cross-Entropy Loss.
 - Early stopping, model checkpointing and lerning rate reduction callbacks were used for optimization and preventing overfitting.

 #### Performace Metics:
 - **Accuracy:** Model achieved an accuracy of approx. 68% on validation set.
 - **Precision:** Precision scroe is ~68%.
 - **Recall:** Recall Score is ~68%.
 - **F1 Score:** F1 Score is ~67%.

 #### Confusion Matrix:
 - Confusion matrix revealed that certain class, such as `Plastic` and `Food_Waste`, are classified more accurately that others due to class imbalance.

## Conclusion

1. **Data-related Improvements**
   - Implement data augmentation to address class imbalance
   - Collect more samples for underrepresented classes (especially Cardboard)
   - Include more diverse images within each category

2. **Model Enhancements**
   - Experiment with deeper architectures or pre-trained models
   - Implement class weights to handle imbalanced data
   - Try different optimization strategies and hyperparameters

3. **Practical Applications**
   - Could be integrated into automated waste sorting systems
   - Potential for mobile applications for consumer waste sorting
   - Useful for recycling facilities and waste management education

This demonstrates the potential of CNN-based approaches for waste segregation while highlighting areas for future improvement in both data collection and model architecture.

## References Used:
1. Upgrads Content & Started Notebook
2. [Image Preprocessing in TensorFlow](https://www.tensorflow.org/tutorials/load_data/images)
3. [Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)
4. [Understanding One-Hot Encoding](https://towardsdatascience.com/understanding-one-hot-encoding-and-its-importance-in-machine-learning-cf8fb0ab73b4)
5. [Building a CNN in Keras](https://www.tensorflow.org/tutorials/images/cnn)
6. [Evaluating Classification Models](https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/)
   

