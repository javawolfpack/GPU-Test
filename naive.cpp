#include <cstdio>
#include <omp.h>
#include <stdexcept>
#include <string>
#include <random>


//Basic function taken from example here: https://stackoverflow.com/questions/28962655/can-openmp-be-used-for-gpus
void vadd2(int n, float * a, float * b, float * c){
  for(int i = 0; i < n; i++){
      c[i] = a[i] + b[i];
  }
}

int main(int argc, char *argv[]){
  if(argc < 2) {
    printf("You must provide at least one argument\n");
    exit(0);
  }
  std::string arg = argv[1];
  try {
    std::size_t pos;
    int n = std::stoi(arg, &pos);
    if (pos < arg.size()) {
      std::cerr << "Trailing characters after number: " << arg << '\n';
    }
    float a[n], b[n], c[n];
    std::random_device rd;
    std::mt19937 e2(rd());
    std::uniform_real_distribution<> dist(0, 100);
    for(int i = 0; i < n; i++){
      a[i] = dist(e2);
      b[i] = dist(e2);
      std::cout << a[i] << " " << b[i]<< "\n";
    }


  } catch (std::invalid_argument const &ex) {
    std::cerr << "Invalid number: " << arg << '\n';
  } catch (std::out_of_range const &ex) {
    std::cerr << "Number out of range: " << arg << '\n';
  }
}
