module TwobitCounter(rst,clk,Cnt4);

input rst;
input clk;
output [1:0] Cnt4;

wire  w1;
wire  w2;
wire  w3;
wire  w4;
wire [1:0] b5;
wire  b5_1;
wire  b5_1_w7;
wire  b5_0;
wire  b5_0_w6;

assign w1 = rst;
assign w2 = clk;
assign Cnt4 = b5;

assign b5[1] = b5_1;
assign b5[0] = b5_0;

assign b5_1_w7 = {b5[1]};
assign b5_0_w6 = {b5[0]};

PNU_DFF
     s0 (
      .reset(w1),
      .clock(w2),
      .Q(w3),
      .D(b5_0_w6));

PNU_DFF
     s1 (
      .reset(w1),
      .clock(w2),
      .Q(w4),
      .D(b5_1_w7));

PNU_NOT
     s2 (
      .i1(w3),
      .o1(b5_0));

PNU_XOR2
     s3 (
      .i2(w3),
      .i1(w4),
      .o1(b5_1));

endmodule

