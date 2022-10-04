#include "c_img.h"
#include "seamcarving.h"
#include <stdio.h>
#include <math.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

void calc_energy(struct rgb_img *im, struct rgb_img **grad){

    int r_x, r_y, g_x, g_y, b_x, b_y, d_x, d_y, e_pixel, e_gradient;

    create_img(grad, im->height, im->width);

    for (int y = 0; y < im->height; y++){
        for (int x = 0; x < im->width; x++){

            //top of the image
            if (y == 0){
                r_y = get_pixel(im, (im->height) - 1, x, 0) - get_pixel(im, y + 1, x, 0);
                g_y = get_pixel(im, (im->height) - 1, x, 1) - get_pixel(im, y + 1, x, 1);
                b_y = get_pixel(im, (im->height) - 1, x, 2) - get_pixel(im, y + 1, x, 2);

            }
            //bottom of the image
            else if (y == (im->height) - 1){
                r_y = get_pixel(im, y - 1, x, 0) - get_pixel(im, 0, x, 0);
                g_y = get_pixel(im, y - 1, x, 1) - get_pixel(im, 0, x, 1);
                b_y = get_pixel(im, y - 1, x, 2) - get_pixel(im, 0, x, 2);
            }
            //between (vertical)
            else{
                r_y = get_pixel(im, y - 1, x, 0) - get_pixel(im, y + 1, x, 0);
                g_y = get_pixel(im, y - 1, x, 1) - get_pixel(im, y + 1, x, 1);
                b_y = get_pixel(im, y - 1, x, 2) - get_pixel(im, y + 1, x, 2);
            }


            //left of the image
            if (x == 0){
                r_x = get_pixel(im, y, (im->width) - 1, 0) - get_pixel(im, y, x + 1, 0);
                g_x = get_pixel(im, y, (im->width) - 1, 1) - get_pixel(im, y, x + 1, 1);
                b_x = get_pixel(im, y, (im->width) - 1, 2) - get_pixel(im, y, x + 1, 2);

            }
            //right of the image
            else if (x == (im->width)-1){
                r_x = get_pixel(im, y, x - 1, 0) - get_pixel(im, y, 0, 0);
                g_x = get_pixel(im, y, x - 1, 1) - get_pixel(im, y, 0, 1);
                b_x = get_pixel(im, y, x - 1, 2) - get_pixel(im, y, 0, 2);
            }
            //between (horizontal)
            else{
                r_x = get_pixel(im, y, x - 1, 0) - get_pixel(im, y, x + 1, 0);
                g_x = get_pixel(im, y, x - 1, 1) - get_pixel(im, y, x + 1, 1);
                b_x = get_pixel(im, y, x - 1, 2) - get_pixel(im, y, x + 1, 2);
            }
			d_x = r_x*r_x + g_x*g_x + b_x*b_x;
			d_y = r_y*r_y + g_y*g_y + b_y*b_y;
			e_pixel = sqrt(d_x + d_y);
			e_gradient = (uint8_t)(e_pixel / 10);
			set_pixel(*grad, y, x, e_gradient, e_gradient, e_gradient);
        }
    }
}


void dynamic_seam(struct rgb_img *grad, double **best_arr){

    //Allocate
    *best_arr = malloc((grad->height)*(grad->width) * sizeof(double));

    int height = grad-> height;
    int width = grad->width;


    for (int i = 0; i < width; i++){
        (*best_arr)[i] = grad->raster[3 * i];
    }
    for (int i = 1 ; i < grad->height; i++){
        for (int j = 0; j < grad->width; j++){
            if (j == 0){
                (*best_arr)[i * width + j] = (double)grad->raster[3 * (i * (grad->width) + j)] +
                (double)MIN((*best_arr)[(i - 1) * width + j], (*best_arr)[(i - 1) * width + (j + 1)]);
            }

            else if (j == (width - 1)){
                (*best_arr)[i * width + j] = (double)grad->raster[3 * (i * (grad->width) + j)] +
                (double)MIN((*best_arr)[(i - 1) * width + j], (*best_arr)[(i - 1) * width + (j - 1)]);
            }

            else{
                double min = MIN((*best_arr)[(i - 1) * width + j], (*best_arr)[(i - 1) * width + (j - 1)]);

                (*best_arr)[i * width + j] = (double)grad->raster[3 * (i * (grad->width) + j)] +
                (double)MIN(min, (*best_arr)[(i-1) * width + (j + 1)]);
            }
        }
    }


}


void recover_path(double *best, int height, int width, int **path){
	int min = 0;
	*path = (int*) malloc(height*sizeof(int));
	for(int i = height -1 ; i >= 0 ; i--){
		if(i == height -1){
			for(int j = 0; j< width ; j++){
				if(*((best+i*width) + j) < *((best+i*width) + min)){
					min = j;
				}
			}
			*(*(path) +i) = min;

		}
		else{
			min = *(*(path) +i+1);
			for(int j = -1 ; j < 2 ; j ++){
				if(min + j < 0 || min + j>= width ){
					continue;
				}
				else{
					if( *((best+i*width) + *(*(path) +i+1) +j) < *((best+i*width) + min)){
						min = *(*(path) +i+1) +j;
					}
				}
			}
			*(*(path) + i) = min;
		}
	}

}
void remove_seam(struct rgb_img *src, struct rgb_img **dest, int *path){
	create_img(dest, src->height , src->width -1);
	for(int i = 0 ; i < src->height ; i++){
		int min1 = 0;
		for(int j = 0 ; j < src->width ; j++){
			if(j == *(path+i)){
				min1 =1;
			}
			else{
				set_pixel(*dest,i , j-min1, get_pixel(src, i, j ,0) ,  get_pixel(src, i, j ,1)  , get_pixel(src, i, j ,2)  );
			}
		}
	}

}
