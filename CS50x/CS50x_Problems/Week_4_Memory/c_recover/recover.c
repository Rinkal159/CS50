#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    uint8_t buffer[512];

    FILE *output = NULL;
    char filename[8];
    int jpeg_count = 0;
    int is_jpeg = 0;

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (is_jpeg)
            {
                fclose(output);
            }
            else
            {
                is_jpeg = 1;
            }

            sprintf(filename, "%03d.jpg", jpeg_count);

            output = fopen(filename, "w");
            if (output == NULL)
            {
                fclose(card);
                return 1;
            }

            jpeg_count++;
        }

        if (is_jpeg)
        {
            fwrite(buffer, sizeof(uint8_t), 512, output);
        }
    }

    fclose(output);
    fclose(card);
}
