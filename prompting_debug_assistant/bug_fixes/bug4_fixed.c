#include <stdio.h>

int main(void)
{
    int numbers[5] = {1, 2, 3, 4, 5};
    int sum = 0;
    int i;

    for (i = 0; i < 5; i++)
    {
        sum += numbers[i];
    }

    printf("Sum: %d\n", sum); /* expected: 15 */
    return 0;
}
