# final-year-v2

While the Internet offers great flexibility in the transmission of multimedia, it also offers oppurtunities for unscrupulous individuals to violate copyright or to commit forgery. One method of overcoming this problem is to embed the copyright information into the data being transmitted such that the data may be recovered at the other end of the transmission. This task is under the purview of steganography.

Since their inception, Field Programmable Gate Arrays (FPGAs) have provided hardware designers great flexibility in designing custom hardware to accommodate hard deadline requirements. In addition to custom hardware for hard deadline requirements, FPGAs also occupy a niche in high performance computing - by exploiting the specificity and inherent parallelism of FPGAs, we can sped up the performance of computationally intensive tasks. In this project, we shall design custom hardware in VHDL to run on a Xilinx Spartan 3E FPGA that embodies a reversible VQ index based steganographic technique designed by Kieu et al.

Following the work of Kieu et al, we designed two circuits: an encoder and a decoder. To simplify our implementation of our algorithm, we defined the hilbert curve index table as our starting point and end point for the encoder and decoder respectively. Moreover, we loaded the input data into block RAM that was defined using the IP Core Generator of ISE 14.1.

For development, we used the Diligent Basys and Nexus2 boards containing Xilinx Spartan 3E XC3S250E and XC3S500E respectively.

## Encoder

Upon using the VHDL code in this repository to syntheisize and simulate the design, we completed the process of encoding the VQ indicies along with secret bits in 8000000 ns. We achieved the following utilization statisitcs:
