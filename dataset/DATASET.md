
# Dataset Information

## Project
Vision-Based Object Detection for an Autonomous Vehicle

## Phase 2 Dataset Status

Phase 1 proposed a 13-class autonomous-vehicle detection system.

For the Phase 2 implementation, a pretrained YOLO11n model was evaluated using the Ultralytics COCO8 validation dataset as a pipeline and baseline evaluation dataset.

COCO8 was used to verify:
- Model loading
- GPU-based inference
- Training pipeline
- Validation pipeline
- Detection visualization
- Evaluation plot generation

## Road-Relevant Classes

The pretrained YOLO11n model contains several classes relevant to the proposed autonomous-vehicle system:

| Phase 1 Requirement | YOLO Class |
|---|---|
| Pedestrian | person |
| Bicyclist | bicycle |
| Two-wheeler | motorcycle |
| Cars | car |
| Traffic light | traffic light |

Additional relevant COCO classes include cow, bus, truck and stop sign.

## Dataset Format

YOLO object-detection datasets use the following annotation format:

class_id x_center y_center width height

Coordinates are normalized to the image dimensions.

## Dataset Limitation

The COCO8 dataset is a very small dataset intended primarily for testing the YOLO training and evaluation pipeline.

It does not contain the complete 13-class taxonomy proposed in Phase 1.

Therefore, the current Phase 2 results should be interpreted as a baseline/pipeline validation rather than final 13-class autonomous-vehicle model performance.

## Future Dataset

A larger hybrid road-scene dataset should be assembled using suitable public road datasets and custom annotations for:

- Cone
- Traffic barrier
- Cow
- Pedestrian
- Bicyclist
- Two-wheeler
- Cars
- Red light
- Green light
- Amber light
- Speed 10
- Speed 15
- Speed 30
