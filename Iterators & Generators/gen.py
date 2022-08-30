import time 

gen_start_time = time.time()
print(sum(n for n in range(10000000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000000)]))
lisst_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000000)])) took: {list_time}")