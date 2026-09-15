
# Vision-Based Object Detection for an Autonomous Vehicle

## Phase 02 Implementation

This project implements and evaluates a YOLO-based object-detection pipeline for autonomous-vehicle perception.

The Phase 1 proposal defined a 13-class detection system using stereo-camera input and edge deployment.

## Proposed Classes

1. Cone
2. Traffic barrier
3. Cow
4. Pedestrian
5. Bicyclist
6. Two-wheeler
7. Cars
8. Red light
9. Green light
10. Amber light
11. Speed 10
12. Speed 15
13. Speed 30

## Phase 2 Baseline

For rapid Phase 2 validation, YOLO11n pretrained on the COCO dataset was used.

The baseline contains several relevant road-scene classes:

- person
- bicycle
- car
- motorcycle
- traffic light

The implementation validates the complete model inference and evaluation workflow.

## Technology

- Python
- Ultralytics YOLO
- PyTorch
- OpenCV
- NVIDIA CUDA GPU
- Google Colab

## Output

Each detection provides:

- Bounding box
- Class label
- Confidence score

Bounding box format:

[x_min, y_min, x_max, y_max]

## Project Structure

Phase02_Autonomous_Vehicle/
│
├── src/
│   └── detect.py
│
├── model/
│   └── best.pt
│
├── results/
│   ├── detections/
│   └── evaluation/
│
├── dataset/
│   └── DATASET.md
│
├── requirements.txt
└── README.md

## Inference

Install dependencies:

pip install -r requirements.txt

Run detection:

python src/detect.py --source path/to/image.jpg --conf 0.25

## Evaluation

The YOLO validation pipeline was executed on COCO8.

Generated evaluation artifacts include:

- Confusion matrix
- Precision curve
- Recall curve
- F1 curve
- Precision-Recall curve
- Validation predictions

## Limitations

The current baseline does not implement the complete 13-class taxonomy.

The Phase 1 architecture proposed ZED 2i, Jetson Orin NX, P2 feature processing, ONNX/TensorRT deployment and additional detector benchmarking. These components require further hardware and implementation work and are not claimed as completed in this baseline.

## Future Work

- Assemble a larger road-scene dataset
- Add custom annotations for the complete 13 classes
- Train a custom YOLO11 model
- Investigate P2 feature processing for small traffic signs/lights
- Export to ONNX
- Benchmark TensorRT FP16 and INT8
- Deploy on NVIDIA Jetson Orin NX
- Evaluate performance under blur, glare, low light, dust and occlusion
