# Session Overview

Welcome to this session on **Convolutional Neural Networks (CNNs)**.

This session introduces CNNs and explains why traditional models face challenges when working with image data. You will understand how CNNs are designed to process visual information more effectively.

We will explore how images are represented digitally and introduce the key components of CNNs, such as **layers, filters, and pooling**, showing how these work together to extract useful information from images. You will also learn how each component contributes to recognizing patterns and features in visual data.

You will also understand different CNN architectures, techniques to improve model performance, and approaches like **transfer learning**. This session provides a solid foundation for understanding how CNNs are structured and applied to image-related tasks.

## What You'll Learn

- Why traditional machine learning models struggle with image data
- How images are represented in digital form
- The fundamental components of CNNs:
  - Layers
  - Filters
  - Pooling operations
- How CNNs extract features and identify patterns in images
- Different CNN architectures
- Techniques for improving model performance
- Transfer learning and its applications

## Next Step

Let's begin by exploring the key challenges that traditional machine learning models encounter when handling complex data such as images.
----
# Challenges with ML Models - 1

Let’s begin by understanding the challenges faced by **classical machine learning** models when working with unstructured data. You will also learn how the concept of the **Convolutional Neural Network (CNN)** emerged and how it was inspired by the **visual system of mammals**.

Next, you will gain an understanding of the challenges involved in processing image data using **classical ML models**.

You have already learned how a computer represents black-and-white images as a **matrix of numbers**. Images are divided into many small areas called **Picture Elements (Pixels)**, and each pixel has an associated value. These values represent the intensity of the image at that location, and each pixel corresponds to a very small portion of the image.

Images can also be represented as a **matrix of numerical values**. Computers interpret the features within an image through these pixel values. Each pixel has a different value depending on the **intensity of the image** at that specific location.

> **Note**
>
> Conventionally, higher pixel values are associated with white color, while lower pixel values are associated with black color. However, for the purpose of explanation and visualization, this representation has been reversed in the example.
>
> Pixel values typically range from **0 to 255**:
>
> - **0** represents black
> - **255** represents white
>
> In the SME's example, the values have been used in reverse:
>
> - Black dots are represented by values around **200**
> - Lighter areas are represented by values closer to **0**

You have now learned how an image can be represented as a **matrix of numbers**. Next, you will explore why **classical machine learning models** struggle to work effectively with image data.
