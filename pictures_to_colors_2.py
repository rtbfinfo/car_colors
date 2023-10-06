import cv2
import pandas as pd
import os
import json

def save_colors_to_csv(color_data):
    # Save to CSV
    df = pd.DataFrame(color_data, columns=['Color'])
    df.to_csv('/Users/ambroisecarton/Desktop/cars_frames/colors.csv', index=False)

def main():
    # Initialize
    image_dir = '/Users/ambroisecarton/Desktop/cars_frames/lundi'
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.jpg')])
    total_images = len(image_files)
    processed_images = 0
    color_data = []
    progress_file = "/Users/ambroisecarton/Desktop/cars_frames/progress.json"

    # Load progress if progress file exists
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            progress = json.load(f)
            processed_images = progress['processed_images']
            color_data = progress['color_data']

    def get_color(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            color = image[y, x].tolist()  # BGR format
            color_data.append('#{:02x}{:02x}{:02x}'.format(color[2], color[1], color[0]))  # Convert to HTML color code

    for image_file in image_files[processed_images:]:
        image_path = os.path.join(image_dir, image_file)
        image = cv2.imread(image_path)
        cv2.setMouseCallback('Image', get_color)

        while True:
            info_text = f'Image {processed_images + 1}/{total_images} ({image_file}) - Colors saved: {len(color_data)}'
            img_display = image.copy()
            cv2.putText(img_display, info_text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow('Image', img_display)
            
            key = cv2.waitKey(1)
            if key == 13:  # Enter key
                processed_images += 1
                break
            elif key == ord('q'):  # 'q' key for quit
                # Save progress
                progress = {
                    'processed_images': processed_images,
                    'color_data': color_data
                }
                with open(progress_file, 'w') as f:
                    json.dump(progress, f)
                save_colors_to_csv(color_data)  # Save colors to CSV on quit
                cv2.destroyAllWindows()
                return

    cv2.destroyAllWindows()  # Make sure to close any remaining windows
    save_colors_to_csv(color_data)  # Save colors to CSV on complete

    # Delete progress file if exists
    if os.path.exists(progress_file):
        os.remove(progress_file)

if __name__ == '__main__':
    main()
