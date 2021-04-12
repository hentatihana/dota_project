from tqdm import tqdm

from data_utils import convert_to_jpeg, get_file_from_this_rootdir


# source_dir = '/content/dota_project/data/dota/train_1024/images'
source_dir = '/content/dota_project/data/dota/val_1024/images'
# save_dir = '/content/dota_project/data/dota/train_1024/images_jpg/'
save_dir = '/content/dota_project/data/dota/val_1024/images_jpg/'


if __name__ == '__main__':
    filepath_list = get_file_from_this_rootdir(source_dir, 'png')
    for file in tqdm(filepath_list):
        convert_to_jpeg(file, save_dir)
    print('covert image type to JPEG - Done!!!!!')