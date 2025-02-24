""" SAM (Segmentation and Masking) model for image segmentation and object detection. """
import os
import numpy as np
import torch
from mobile_sam import SamAutomaticMaskGenerator, SamPredictor, sam_model_registry
from PIL import Image

# from app.tools.tools import box_prompt, format_results, point_prompt
# from app.tools.tools_gradio import fast_process

'''
libraries:

torch
torchvision
timm
opencv-python
git+https://github.com/dhkim2810/MobileSAM.git
matplotlib
'''
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

sam_checkpoint = "./mobile_sam.pt"
model_type = "vit_t"

mobile_sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
mobile_sam = mobile_sam.to(device=device)
mobile_sam.eval()

mask_generator = SamAutomaticMaskGenerator(mobile_sam)
predictor = SamPredictor(mobile_sam)

@torch.no_grad()
def segment_everything(
    image,
    input_size=1024,
    better_quality=False,
    with_contours=True,
    use_retina=True,
    mask_random_color=True,
):
    """ Segment an image using the SAM model. """
    global mask_generator

    input_size = int(input_size)
    w, h = image.size
    scale = input_size / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = image.resize((new_w, new_h))

    nd_image = np.array(image)
    annotations = mask_generator.generate(nd_image)
    return annotations

    # this function is to overlays the segmentation masks and contours onto the image
    # fig = fast_process(
    #     annotations=annotations,
    #     image=image,
    #     device=device,
    #     scale=(1024 // input_size),
    #     better_quality=better_quality,
    #     mask_random_color=mask_random_color,
    #     bbox=None,
    #     use_retina=use_retina,
    #     withContours=with_contours,
    # )
    # return fig



if __name__ == "__main__":
    input_path = "resources/dog.jpg"
    output_path = "generated/output.png"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    image = Image.open(input_path).convert("RGB")
    fig = segment_everything(
        image=image
    )
    fig.save(output_path)
