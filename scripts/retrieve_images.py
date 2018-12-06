#!/usr/bin/env python 

import glob
import os 

if __name__ == '__main__':

    input_dir = '/Users/davidriser/repos/python-analysis/kaon-bsa/image'
    target_dir = '/Users/davidriser/repos/kaon-note/image/plots/kaon-bsa'

    image_extensions = ['pdf', 'png']

    images_needed = {}
    images_found = {}
    images_missing = {}

    # for each type of image we're looking for
    # check the target and see what we are looking 
    # to copy 
    for ext in image_extensions:
        images_needed[ext] = glob.glob('{}/*.{}'.format(target_dir, ext))
        source_images = glob.glob('{}/*.{}'.format(input_dir, ext))

        # strip the path off 
        images_needed[ext] = [image.split('/')[-1] for image in images_needed[ext]]
        source_images = [image.split('/')[-1] for image in source_images]

        # start keeping track for this extension 
        images_found[ext] = []
        images_missing[ext] = []

        for image in images_needed[ext]:
            if image in source_images:
                images_found[ext].append(image)
                print('Copied {}'.format(image))
                os.system('cp {}/{} {}/{}'.format(
                        input_dir, image, target_dir, image))
            else:
                images_missing[ext].append(image)
                print('Could not find {}'.format(image))

