from PIL import Image, ImageFilter
import os

def process_images(input_folder):
    # Get the current working directory
    current_directory = os.getcwd()

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(current_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for i, image_file in enumerate(image_files):
        # Open the original image
        original_path = os.path.join(current_directory, image_file)
        original_image = Image.open(original_path)

        # Calculate new dimensions to fit within 1280x720 while maintaining aspect ratio
        original_width, original_height = original_image.size
        aspect_ratio = original_width / original_height

        if aspect_ratio > 1280 / 720:
            new_width = 1280
            new_height = int(1280 / aspect_ratio)
        else:
            new_width = int(720 * aspect_ratio)
            new_height = 720

        # Resize the original image to the calculated dimensions
        resized_image = original_image.resize((new_width, new_height))

        # Resize the original image to 80% of its size
        resized_image = resized_image.resize((int(new_width * 0.8), int(new_height * 0.8)))

        # Blur the original image with a higher radius for more pronounced blur
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=10))

        # Create a new image with an alpha channel
        final_image = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))

        # Calculate paste locations to center both images
        blur_paste_location = ((1280 - blurred_image.width) // 2, (720 - blurred_image.height) // 2)
        resized_paste_location = ((1280 - resized_image.width) // 2, (720 - resized_image.height) // 2)

        # Paste the blurred image onto the new image
        final_image.paste(blurred_image, blur_paste_location)

        # Paste the resized image with alpha channel onto the new image
        alpha_mask = Image.new('L', resized_image.size, 255)
        final_image.paste(resized_image.convert('RGBA'), resized_paste_location, alpha_mask)

        # Save the final image with a new name in the same folder
        output_path = os.path.join(current_directory, f"childhood{i+1}.png")
        final_image.save(output_path)

if __name__ == "__main__":
    process_images(os.getcwd())
    print("Image processing complete.")
