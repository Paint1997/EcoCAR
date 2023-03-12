from mmdet.apis import init_detector, inference_detector
img = 'demo/Carla_Test.jpg'

config_file = 'yolov3_mobilenetv2_320_300e_coco.py'
checkpoint_file = 'yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or device='cuda:0'
result = inference_detector(model, img)
model.show_result(img, result, out_file= 'result1.jpg')


