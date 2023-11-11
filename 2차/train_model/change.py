from PIL import Image


def flip_image(input_path, output_path):
    # 이미지 열기
    img = Image.open(input_path)

    # 이미지 좌우 반전
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # 반전된 이미지 저장
    flipped_img.save(output_path)


if __name__ == "__main__":
    # 입력 이미지 경로와 출력 이미지 경로 설정
    input_image_path = "../놀라움/놀란동양남자1.jpg"  # 입력 이미지 파일명을 실제 파일명으로 변경
    output_image_path = "../놀라움/놀란동양남자1_1.jpg"  # 출력 이미지 파일명을 실제 파일명으로 변경

    # 이미지 좌우 반전 함수 호출
    flip_image(input_image_path, output_image_path)

    print("이미지가 성공적으로 좌우로 반전되었습니다.")
