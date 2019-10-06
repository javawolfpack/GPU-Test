//benchmark library from Google: https://github.com/google/benchmark
#include <benchmark/benchmark.h>
#include<iostream>
#include<climits>
#include <random>

using namespace std;

// Global variables for array with size of 1000


/* Kadane MSP Implementation */

int maxSubArraySumKadane(int a[], int size)
{
	int max_so_far = INT_MIN, max_ending_here = 0;

	for (int i = 0; i < size; i++)
	{
		max_ending_here = max_ending_here + a[i];
		if (max_so_far < max_ending_here)
			max_so_far = max_ending_here;

		if (max_ending_here < 0)
			max_ending_here = 0;
	}
	return max_so_far;
}

/* Divide and Conquer MSP Implementation */

// // A utility funtion to find maximum of two integers
// int max(int x, int y) { return (x > y)? x : y; }

// // A utility funtion to find maximum of three integers
// int max(int x, int y, int z) { return max(max(x, y), z); }

// // Find the maximum possible sum in arr[] such that arr[m] is part of it
// int maxCrossingSum( int l ,     // leftmost index
//                     int m ,     // middle index
//                     int h )     // rightmost index
// {
// 	// Include elements on left of mid.
// 	int sum = 0;
// 	int left_sum = INT_MIN;
// 	for (int i = m; i >= l; i--)
// 	{
// 		sum = sum + a[i];
// 		if (sum > left_sum)
// 		left_sum = sum;
// 	}

// 	// Include elements on right of mid
// 	sum = 0;
// 	int right_sum = INT_MIN;
// 	for (int i = m+1; i <= h; i++)
// 	{
// 		sum = sum + a[i];
// 		if (sum > right_sum)
// 		right_sum = sum;
// 	}

// 	// Return sum of elements on left and right of mid
// 	return left_sum + right_sum;
// }

// // Returns sum of maxium sum subarray in arr[l..h]
// int maxSubArraySumDC( int l ,     // leftmost index
//                     int h )     // rightmost index
// {
// // Base Case: Only one element
// if (l == h)
// 	return a[l];

// // Find middle point
// int m = (l + h)/2;

// /* Return maximum of following three possible cases
// 	a) Maximum subarray sum in left half
// 	b) Maximum subarray sum in right half
// 	c) Maximum subarray sum such that the subarray crosses the midpoint */
// return max( maxSubArraySumDC( l , m ),
// 		    maxSubArraySumDC( m+1 , h ),
// 		    maxCrossingSum( l , m , h ) );
// }

/* Naive MSP Implementation */
int maxSubArraySumNaive(int a[], int size)
{
  int max_sum = INT_MIN;
  // check if best option is to buy on first day & sell on second day,
  // then check total sum the next day to see if that value is higher
  for (int start = 0; start < size-1; start++){
    int change = a[start];
    if(change > max_sum){
      max_sum = change;
    }
    for(int end = start + 1; end < size; end++){
      change = a[end] + change;
      if(change > max_sum){
        max_sum = change;
      }
    }
  }
  return max_sum;
}

// Generate random array (size 1000) with values distributed between -100 & 100
// void generate(){
//   a = new int [size];
//   std::random_device rd;
//   std::mt19937 e2(rd());
//   std::uniform_real_distribution<> dist(-100, 100);
//   for(int i = 0; i < size; i++){
//     a[i] = dist(e2);
//     // cout << a[i] << " ";
//   }
//   // cout << endl;
// }

// Driver program to test maxSubArraySum
// int main()
// {
// 	// int a[] = {-2, -3, 4, -1, -2, 1, 5, -3};
//   // //int a[] = {13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
// 	// int n = sizeof(a)/sizeof(a[0]);
//   generate();
// 	int max_sum = maxSubArraySum();
// 	cout << "Maximum contiguous sum is " << max_sum;
//
// 	return 0;
// }

// static void BM_Generate(benchmark::State& state) {
//   // Perform setup here
  
//   for (auto _ : state) {
//     // This code gets timed
//     generate();
//   }
// }

static void BM_mspkadane(benchmark::State& state) {
  // Perform setup here
  int* a = new int[state.range(0)];
  int size = state.range(0);
  for (auto _ : state) {
    // This code gets timed
    maxSubArraySumKadane(a, size);
  }
}

// static void BM_mspDC(benchmark::State& state) {
//   // Perform setup here
//   for (auto _ : state) {
//     // This code gets timed
//     maxSubArraySumDC(0,size-1);
//   }
// }

static void BM_mspnaive(benchmark::State& state) {
  // Perform setup here
  int* a = new int[state.range(0)];
  int size = state.range(0);
  for (auto _ : state) {
    // This code gets timed
    maxSubArraySumNaive(a, size);
  }
}

// BENCHMARK(BM_Generate);
BENCHMARK(BM_mspkadane)->Range(8, 8<<10);
// BENCHMARK(BM_mspDC);
BENCHMARK(BM_mspnaive)->Range(8, 8<<10);
// Run the benchmark
BENCHMARK_MAIN();
