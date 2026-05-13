#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg =
                round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int newRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                               .189 * image[i][j].rgbtBlue);
            newRed = newRed > 255 ? 255 : newRed;

            int newGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                                 .168 * image[i][j].rgbtBlue);
            newGreen = newGreen > 255 ? 255 : newGreen;

            int newBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                                .131 * image[i][j].rgbtBlue);
            newBlue = newBlue > 255 ? 255 : newBlue;

            image[i][j].rgbtRed = newRed;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtBlue = newBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int low = j;
            int high = width - 1 - j;

            int leftRed = image[i][low].rgbtRed;
            int leftGreen = image[i][low].rgbtGreen;
            int leftBlue = image[i][low].rgbtBlue;

            int rightRed = image[i][high].rgbtRed;
            int rightGreen = image[i][high].rgbtGreen;
            int rightBlue = image[i][high].rgbtBlue;

            image[i][low].rgbtRed = rightRed;
            image[i][low].rgbtGreen = rightGreen;
            image[i][low].rgbtBlue = rightBlue;

            image[i][high].rgbtRed = leftRed;
            image[i][high].rgbtGreen = leftGreen;
            image[i][high].rgbtBlue = leftBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // createing copy of the original image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int row[] = {i - 1, i - 1, i - 1, i, i, i, i + 1, i + 1, i + 1};
            int col[] = {j - 1, j, j + 1, j - 1, j, j + 1, j - 1, j, j + 1};

            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;

            int count = 0;

            for (int k = 0; k < 9; k++)
            {
                if (row[k] >= 0 && row[k] < height && col[k] >= 0 && col[k] < width)
                {
                    sumRed += copy[row[k]][col[k]].rgbtRed;
                    sumGreen += copy[row[k]][col[k]].rgbtGreen;
                    sumBlue += copy[row[k]][col[k]].rgbtBlue;

                    count++;
                }
            }

            image[i][j].rgbtRed = round((float)sumRed / count);
            image[i][j].rgbtGreen = round((float)sumGreen / count);
            image[i][j].rgbtBlue = round((float)sumBlue / count);
        }
    }

    return;
}
