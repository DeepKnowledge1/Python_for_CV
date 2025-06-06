# 🧠 Python for Computer Vision: Build Your Own Image Toolkit from Scratch

A hands-on course where you'll learn how to **build your own image processing toolkit in Python**, tailored for **real-world computer vision tasks**. From loading images to simulating defects and preparing datasets for deep learning — this course gives you the tools to do it all (and ship your own CLI tool at the end!).

<img src="bg.png" alt="bg" width="100%" /></a>


## ✅ Legend

- ✅ Uploaded & Completed
- 🔄 In Progress / Not Uploaded Yet

## ✅ What You'll Learn

- 🔍 Python & Computer Vision Fundamentals
- 📁 Dataset Management & Organization
- 🖼️ Image Preprocessing & Manipulation
- 🧮 Essential CV Algorithms
- 🔄 Advanced Computer Vision Techniques
- 🎭 Data Augmentation & Simulation
- 📊 Analysis & Validation
- ⚡ Performance Optimization
- 🔧 Tools & Integration

## 🚀 By the End, You'll Have:
A fully working `cv_toolkit.py` script that lets you run commands like:
```bash
python cv_toolkit.py --input ./raw --resize 256x256 --grayscale --add_scratches --output ./processed
```

## 💡 Perfect For:
- 🔍 Complete beginners to programming
- 🤖 Python developers new to CV
- 🛠️ Anyone building personal or production-level vision projects

---

## 📚 Course Structure

### PART 1: FOUNDATIONS (For Complete Beginners)

#### 📁 Section 1: Introduction to Programming & Computer Vision
*Videos 1-7*

| Status | Title                                                                   |
| ----- | ----------------------------------------------------------------------- |
| ✅ | 📦 Introduction    [🎥 Watch Video](https://youtu.be/tAumg8Odcm4) | [💻 Code Example](No)     |
| ✅ | 📦 What is Computer Vision & Why Python? + Real-World Use Cases    [🎥 Watch Video](https://youtu.be/trL2qIfpY3U) | [💻 Code Example](No)     |
| ✅ | 🛠️ Installing Python & Tools You Need – With Common Pitfalls & Fixes [🎥 Watch Video](https://youtu.be/ocVk_B-ivHQ) | [💻 Code Example](No)   |
| ✅ | 🎵 Modern Dependency Management with Poetry [🎥 Watch Video](https://youtu.be/F5sdNXb2P98) | [💻 Code Example]("No")|
| ✅ | 🔍 Code Quality with Pre-commit Hooks [🎥 Watch Video](https://youtu.be/yLKmW7zjTwM)                                  |
| ✅ | 🧪 Running Your First Image Script – "Hello World" for CV  [🎥 Watch Video](https://youtu.be/JUHTCel4U4E  )            |
| 🔄 | 🧭 Course Roadmap – How to Get the Most Out of This Playlist            |

---

#### 📁 Section 2: Python Fundamentals Through Image Examples
*Videos 8-14*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| ✅ | 🔢 Variables, Numbers & Strings [🎥 Watch Video](https://youtu.be/2cp5OEHMoNQ) | [💻 Code Example](Sec2_Core_Python_CV/Variables_Numbers_Strings_CV.ipynb) |
| ✅ | ➡️ If Statements & Loops      [🎥 Watch Video](https://youtu.be/HpEgJsQHFWY) | [💻 Code Example](Sec2_Core_Python_CV/IF_LOOP.ipynb) |
| ✅ | 📋 Lists[🎥 Watch Video](https://youtu.be/svcXGLx7PIY) | [💻 Code Example](Sec2_Core_Python_CV/lists.ipynb) |
| ✅ | 📋 Tuple[🎥 Watch Video](https://youtu.be/u45nm0G2Wbg) | [💻 Code Example](Sec2_Core_Python_CV/tuples_notebook.ipynb) |
| ✅ | 📋 Dictionaries[🎥 Watch Video](https://youtu.be/HpEgJsQHFWY) | [💻 Code Example](Sec2_Core_Python_CV/dictionaries_notebook.ipynb) |
| ✅ | 🔁 Functions[🎥 Watch Video](https://youtu.be/zGBIQAHH168) | [💻 Code Example](Sec2_Core_Python_CV/functions_notebook.ipynb) |
| ✅ | 🔄 Working with Files & Directories [🎥 Watch Video](https://youtu.be/SX7hklop9gg) | [💻 Code Example](Sec2_Core_Python_CV/Files_DIR_%20Tutorial.ipynb) |
| ✅ | ⚠️ Error Handling & Debugging [🎥 Watch Video](https://youtu.be/C6vlF4-xXm4)| [💻 Code Example](Sec2_Core_Python_CV/Error_handling.ipynb) |
| 🔄 |📊 🧪 Quiz Time: Test Your Python Knowledge So [🎥 Watch Video]| [💻 Code Example]



---

#### 📁 Section 3: First Steps with Images
*New section combining basics*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| ✅ | 📷 How Computers See Images - Pixels, RGB, Channels [🎥 Watch Video](https://youtu.be/mkel9UVOWSw)| [💻 Code Example] |
| ✅ | 📥 Load & Show Images Using OpenCV & Pillow [🎥 Watch Video](https://youtu.be/a9ITIB2TFoI) | [💻 Code Example](Sec3_Working_with_Images/OpenCV_PILLOW.ipynb) |
| ✅ | 📐 Basic Transformations: Resize, Crop, Rotate      [🎥 Watch Video](https://youtu.be/tOqTAG3i2_o) | [💻 Code Example](Sec3_Working_with_Images/OpenCV_PILLOW_Advance.ipynb) |
| ✅ | 🌈 Understanding Color Spaces                       [🎥 Watch Video](https://youtu.be/HLSIKaqfyKs)| [💻 Code Example](Sec3_Working_with_Images/color_spaces_tutorial.ipynb) |
| ✅ | 📸 Mini Project: Simple Image Processing            [🎥 Watch Video](https://youtu.be/TaQH8pXRzTw)| [💻 Code Example](Sec3_Working_with_Images/sec3_project.py) |

### PART 2: BUILDING BLOCKS

#### 📁 Section 4: Object-Oriented Programming for CV
*Videos 20-29*

| Status | Title                                                                      | Code Example                                      |
| ----- | -------------------------------------------------------------------------- | ------------------------------------------------- |
| ✅ | 🚪 What is OOP? Why It Matters for Computer Vision                         [🎥 Watch Video](https://youtu.be/KMQqxsimMBU)|  |
| ✅ | 📦 Classes vs Functions – When to Use Which                                [🎥 Watch Video](https://youtu.be/ZKUZnlT3zWc)| [💻 Code Example](Sec4_OOP_in_CV/02_classes_vs_functions.ipynb) |
| ✅ | 🛠️ Defining Your First Class                            [🎥 Watch Video](https://youtu.be/kI_JrnydPzI)| [💻 Code Example](Sec4_OOP_in_CV/python_classes.ipynb) |
| ✅ | 🧱 Attributes & Methods – Organizing Image Transformations[🎥 Watch Video](https://youtu.be/kI_JrnydPzI)| [💻 Code Example](Sec4_OOP_in_CV/python_classes.ipynb) |
| ✅ | 🗝️ Constructors (`__init__`) and Default Settings[🎥 Watch Video](https://youtu.be/kI_JrnydPzI)| [💻 Code Example](Sec4_OOP_in_CV/python_classes.ipynb) |
| ✅ | 🎯 Mini Project: Build an Image Processor with Load–Transform–Save Methods [🎥 Watch Video](https://youtu.be/qehAaqFa_6g)| [💻 Code Example](Sec4_OOP_in_CV/ImageProcessor.py) |

#### 📁 Section 4A: Advanced Pythonic OOP
*Videos 26-36*

| Status | Title                                                                      | Code Example                                      |
| ----- | -------------------------------------------------------------------------- | ------------------------------------------------- |
| ✅ | 🔁 Inheritance – Build Specialized Processors from Base Classes            [🎥 Watch Video](https://youtu.be/I6StdtxXBSM)| [💻 Code Example](Sec4Adv_OOP_CV/python_inheritance.ipynb) |
| ✅ | 🔁 Inheritance – Refactoring Image Processor            [🎥 Watch Video](https://youtu.be/OhSswFAM-Ag)| [💻 Code Example](Sec4Adv_OOP_CV/Interitance_refactoring/) |
| 🔄 | 🧙 Magic Methods (Dunder) – Customize Behavior with `__str__`, `__add__`, `__eq__`, etc. |                                     |
| 🔄 | 🎁 Data Classes – Say Goodbye to Boilerplate with `@dataclass`             [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧭 Class vs Static vs Instance Methods – When and Why to Use Each          [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔐 Encapsulation & Property Decorators – Clean Access with `@property` and Getters/Setters |                                   |
| 🔄 | 🌀 Polymorphism – Use One Interface with Many Implementations              [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧱 Abstract Base Classes – Enforce Rules Using `abc.ABC` and `@abstractmethod` |                                               |
| 🔄 | 🧰 Composition Over Inheritance – "Has-a" Relationships for Real-World Modeling |                                              |
| 🔄 | 💼 Build a Professional-Grade `ImagePipeline` Class                        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 OOP Design Patterns for Computer Vision Applications                    [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📝 Mini Project: Complete OOP-Based Image Processing Library               [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 5: Working with Image Files & Folders
*Videos 37-43*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🗂️ Organizing Your Dataset - Folder Structures       [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📁 List All Images in a Folder Recursively           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 Rename, Move & Copy Files Like a Pro              [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ❌ Delete Unwanted Files Safely                      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🖼️ Convert Image Formats in Bulk                    [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 Version Control for Image Datasets                [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📁 Mini Project: Organize Dataset into Splits        [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 6: Essential Image Preprocessing
*Videos 44-49*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 📦 Patchify Large Images into Tiles                  [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ✂️ Crop Images to Region of Interest                 [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎨 Histogram Equalization for Better Contrast        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🖌️ Overlay Masks on Images for Segmentation         [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔀 Normalize Pixel Values for Deep Learning          [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧰 Mini Project: Complete Preprocessing Pipeline     [🎥 Watch Video]| [💻 Code Example] |

### PART 3: CORE CV TECHNIQUES

#### 📁 Section 7: Image Filtering & Edge Detection
*Videos 50-56*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🔍 Introduction to Image Filtering & Kernels         [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔪 Edge Detection: Sobel, Canny, and Laplacian       [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧮 Convolution: How Filters Work Under the Hood      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎯 Corner Detection: Harris & Shi-Tomasi Methods     [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧿 Blob Detection Using Laplacian of Gaussian        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🌀 Advanced Filtering for Denoising                  [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎭 Mini Project: Edge Detection Visualization Tool   [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 8: Feature Detection & Matching
*Videos 57-62*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🔑 Local Features: SIFT, SURF, ORB, and BRIEF        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 Feature Matching Techniques & Distance Metrics    [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🖼️ Image Matching with RANSAC                       [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧩 Creating Image Mosaics with Homography            [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🗝️ Building a Simple Object Recognition System      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Mini Project: Image Matching Application          [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 9: Data Augmentation & Defect Simulation
*Videos 63-68*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🌫️ Add Artificial Noise & Blur to Images            [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📏 Draw Random Lines & Scratches                     [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🌒 Simulate Occlusion & Lighting Changes             [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 Rotate Images for Robustness                      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎞️ Apply Transformations in Real-Time               [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧨 Mini Project: Realistic Defect Simulation         [🎥 Watch Video]| [💻 Code Example] |

### PART 4: ADVANCED TECHNIQUES

#### 📁 Section 10: Segmentation & Shape Analysis
*Videos 69-74*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🧩 Thresholding Techniques                           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Connected Component Analysis & Region Properties  [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📊 Watershed Algorithm for Complex Segmentation      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ➰ Contour Detection & Manipulation                  [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📝 Shape Analysis: Moments, Circularity, Convexity   [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Mini Project: Shape Classifier                    [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 11: Motion Analysis & Video Processing
*Videos 75-79*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🌊 Optical Flow: Lucas-Kanade Method                 [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔄 Dense Optical Flow for Motion Field Estimation    [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎯 Object Tracking Algorithms                        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Background Subtraction for Moving Object Detection[🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🏃 Mini Project: Motion Heatmap Generator            [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 12: Working with Masks & Annotations
*Videos 80-87*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🎭 What Are Binary Masks & Why They Matter           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📐 Generate Masks from Bounding Box Annotations      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎨 Create Synthetic Masks for Objects                [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 👀 Visualize Image-Mask Pairs                        [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📄 Edit Items in JSON Annotation Files               [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Filter Annotations by Class                       [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ⚠️ Check for Missing Images or Labels                [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧪 Mini Project: Annotation File Manipulation Tool   [🎥 Watch Video]| [💻 Code Example] |

### PART 5: OPTIMIZATION & INTEGRATION

#### 📁 Section 13: Dataset Analysis & Quality Control
*Videos 88-92*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 📊 Analyze Image Dimensions Across Dataset           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📈 Plot Class Distribution from Annotations          [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Show Random Samples from Dataset                  [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🗂️ Detect Duplicate Images Automatically            [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📊 Mini Project: Interactive Dataset Analysis Dashboard [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 14: Performance Optimization
*Videos 93-97*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | ⚡ Speed Up Processing with Multiprocessing           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔢 Vectorization Techniques with NumPy               [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🚀 GPU Acceleration for Image Processing             [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 💾 Memory Management for Large Datasets              [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ⏱️ Mini Project: Optimized Preprocessing Pipeline    [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 15: Bridging to Deep Learning
*Videos 98-102*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🔄 When to Use Traditional CV vs. Deep Learning      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧠 Feature Engineering for Neural Networks           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🎯 Improving CNN Performance with Preprocessing      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📈 Hybrid Systems: CV + Neural Networks              [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🔍 Mini Project: Hybrid Object Detection System      [🎥 Watch Video]| [💻 Code Example] |

### PART 6: ADVANCED APPLICATIONS & FINAL PROJECT

#### 📁 Section 16: Anomaly Detection with PaDiM
*Videos 103-107*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🔍 Introduction to PaDiM Algorithm                   [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🛠️ Implementation Details & Step-by-Step Guide      [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | ⚙️ Parameter Optimization for Specific Use Cases     [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📊 Performance Evaluation and Visualization          [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧪 Mini Project: PaDiM-Based Defect Detector         [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 17: Model Validation & Testing
*Videos 108-111*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 📏 Evaluation Metrics for Computer Vision Models     [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧪 Test Dataset Preparation and Validation           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📊 Result Visualization and Interpretation           [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📝 Mini Project: Automated Validation Pipeline       [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 18: Building the Complete CV Toolkit
*Videos 112-115*

| Status | Title                                                          | Code Example                                      |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 🔄 | 🏗️ Architecture Design for the CLI Toolkit          [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 🧩 Component Integration with Modular Approach       [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 💻 Command-line Interface Implementation             [🎥 Watch Video]| [💻 Code Example] |
| 🔄 | 📚 Mini Project: Complete CV Toolkit                 [🎥 Watch Video]| [💻 Code Example] |

#### 📁 Section 19: Next Steps & Advanced Topics
*Videos 116-118*

| Status | Title                                                |
| ----- | ---------------------------------------------------- |
| 🔄 | 🔭 Advanced Computer Vision Topics                   |
| 🔄 | 🏢 Industry Application Case Studies                 |
| 🔄 | 🛣️ Career Paths & Resources for Continued Learning  |

## ✅ Summary

This course provides a comprehensive learning path from basic programming concepts to advanced computer vision techniques. With a strong emphasis on visual learning, hands-on practice, and real-world applications, you'll build a complete image processing toolkit while gaining valuable skills applicable to various computer vision projects.

Each section includes a mini-project that applies the concepts learned, building progressively toward the final CLI toolkit. The course is designed to be accessible to complete beginners while providing depth for those with prior programming experience.
