#include <cstdio>
#include <omp.h>
#include <stdexcept>
#include <string>
#include <random>
#include <iostream>
#include <benchmark/benchmark.h>


//Basic function taken from example here: https://stackoverflow.com/questions/28962655/can-openmp-be-used-for-gpus
void vadd2(int n, float * a, float * b, float * c){
  for(int i = 0; i < n; i++){
      c[i] = a[i] + b[i];
  }
}

void vadd2_opt1(int n, float * a, float * b, float * c){
  #pragma omp parallel for
  for(int i = 0; i < n; i++){
      c[i] = a[i] + b[i];
  }
}

static void BM_naive(benchmark::State& state) {
  // Perform setup here
  float* a = new float[state.range(0)];
  float* b = new float[state.range(0)];
  float* c = new float[state.range(0)];
  int n = state.range(0);
  std::random_device rd;
  std::mt19937 e2(rd());
  std::uniform_real_distribution<> dist(0, 100);
  for(int i = 0; i < n; i++){
    a[i] = dist(e2);
    b[i] = dist(e2);
    // std::cout << a[i] << " " << b[i]<< "\n";
  }
  for (auto _ : state) {
    // This code gets timed
    vadd2(n,a,b,c);
  }
}
static void BM_opt1(benchmark::State& state) {
  // Perform setup here
  float* a = new float[state.range(0)];
  float* b = new float[state.range(0)];
  float* c = new float[state.range(0)];
  int n = state.range(0);
  std::random_device rd;
  std::mt19937 e2(rd());
  std::uniform_real_distribution<> dist(0, 100);
  for(int i = 0; i < n; i++){
    a[i] = dist(e2);
    b[i] = dist(e2);
    // std::cout << a[i] << " " << b[i]<< "\n";
  }
  for (auto _ : state) {
    // This code gets timed
    vadd2_opt1(n,a,b,c);
  }
}

BENCHMARK(BM_naive)->RangeMultiplier(2)->Range(8, 16<<10);
BENCHMARK(BM_opt1)->RangeMultiplier(2)->Range(8, 16<<10);

// Run the benchmark
BENCHMARK_MAIN();


// int main(int argc, char *argv[]){
//   if(argc < 2) {
//     printf("You must provide at least one argument\n");
//     exit(0);
//   }
//   std::string arg = argv[1];
//   try {
//     std::size_t pos;
//     int n = std::stoi(arg, &pos);
//     if (pos < arg.size()) {
//       std::cerr << "Trailing characters after number: " << arg << '\n';
//     }
//     float a[n], b[n], c[n];
//     std::random_device rd;
//     std::mt19937 e2(rd());
//     std::uniform_real_distribution<> dist(0, 100);
//     for(int i = 0; i < n; i++){
//       a[i] = dist(e2);
//       b[i] = dist(e2);
//       // std::cout << a[i] << " " << b[i]<< "\n";
//     }
//     vadd2(n,a,b,c);
//     // float total = 0;
//     // for(int i = 0; i < n; i++){
//     //   total+=c[i];
//     //   // std::cout << a[i] << " " << b[i]<<" " << c[i] <<"\n";
//     // }
//     // std::cout << total << "\n";


//   } catch (std::invalid_argument const &ex) {
//     std::cerr << "Invalid number: " << arg << '\n';
//   } catch (std::out_of_range const &ex) {
//     std::cerr << "Number out of range: " << arg << '\n';
//   }
// }
