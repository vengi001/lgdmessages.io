from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "bg.html", context)

@api_view(['GET'])
def sam(request):
	# CHECKPOINT_PATH='/content/weights/sam_vit_h_4b8939.pth'

	CHECKPOINT_PATH ='/home/suraj/Downloads/sam_vit_h_4b8939.pth'
	import torch
	DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
	MODEL_TYPE = "vit_h"
	from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor


	sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH).to(device=DEVICE)

	breakpoint()
	mask_generator = SamAutomaticMaskGenerator(sam)