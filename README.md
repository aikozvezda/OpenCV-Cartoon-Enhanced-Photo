제 코드에서 먼저 이미지를 그레이스케일했습니다. 그리고 중간값 블러를 적용하여 이미지에서 잡음을 줄였습니다. adapting thresholding을 적용하여 이미지의 엣지를 검출했습니다. 긜고 bilateral filter을 이용하여 이미지를 부드럽게 만들었습니다. bgr에서 hsv로 변환하여 색상 정보를 변경했고, hsv 이미지에서 채도를 1.5배로 증가시켰습니다. 긜고 다시 hsv에서 bgr로 변경했습니다.

저의 알고리즘은 색상 대비가 뚜렷하고 이미지 내에 명확한 가장자리가 있을 때 잘 작동하는 기술을 적용합니다. 예를 들어, 꽃 이미지는 꽃잎과 꽃 중심부 주변에 잘 정의된 가장자리가 보여, 알고리즘이 성공적으로 검정 윤곽선을 만들어내어 만화 효과를 잘 표현했습니다.
![flower](https://github.com/aikozvezda/OpenCV-Cartoon-Enhanced-Photo/assets/144213771/00935d7c-ea99-4792-af3a-4d28645857f3)
![cartoon_enhanced_image](https://github.com/aikozvezda/OpenCV-Cartoon-Enhanced-Photo/assets/144213771/15bb4d12-b634-4c46-8ce8-b0a30f374609)

색상 변환이 섬세하고 가장자리가 뚜렷하지 않은 경우, 알고리즘은 만화 효과를 효과적으로 적용하는 데 어려움을 겪습니다. 예를 들어,개구리 이미지에서 나뭇잎과 개구리 사이의 대비가 강하지 않아 검정 윤곽선이 덜 두드러지고 만화 효과가 잘 나타나지 않습니다.
![nature4](https://github.com/aikozvezda/OpenCV-Cartoon-Enhanced-Photo/assets/144213771/e5a6fd89-6f77-4b66-88d7-e3bfe4c1ccfa)
![cartoon_enhanced_image](https://github.com/aikozvezda/OpenCV-Cartoon-Enhanced-Photo/assets/144213771/53db333b-7b87-47ee-8a6f-fd8a0d999433)

알고리즘의 주요 한계는 만화 스타일 이미지의 특징인 뚜렷한 검정 윤곽선을 만들기 위해 명확하고 대비되는 가장자리에 의존한다는 부분입니다. 이미지에 부드러운 색상 전환 영역이 있거나 대비가 부족하면, 엣지 검출 단계에서 검정선으로 강조할 필요한 경계를 식별하지 못합니다. 개구리 이미지에서 볼 수 있듯이, 알고리즘의 엣지 검출은 배경의 미묘한 녹색 음영을 구별하는 데 실패하여 덜 효과적인 만화 표현을 결과로 낳았습니다.






