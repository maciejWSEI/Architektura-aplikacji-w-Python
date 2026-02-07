The program computes values of the function  
f(x) = cos(x) + ln((x + 1)²)  
for a large range of x values.

The x range is split into smaller fragments.
Each fragment is processed in a separate process using the `multiprocessing` module.

After all processes finish, the results are combined into a single list.
This allows faster computation compared to a single-process approach.
