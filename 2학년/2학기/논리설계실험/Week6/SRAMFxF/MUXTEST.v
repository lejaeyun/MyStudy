module MUXTEST(e,out,i);

input [1:0] e;
output out;
input [3:0] i;

wire  w0;
wire [3:0] b8;
wire [1:0] b6;
wire  b8_3_w2;
wire  b8_2_w3;
wire  b8_1_w4;
wire  b8_0_w5;
wire  b6_0_w7;
wire  b6_1_w8;

assign b6 = e;
assign out = w0;
assign b8 = i;

assign b8_3_w2 = {b8[3]};
assign b8_2_w3 = {b8[2]};
assign b8_1_w4 = {b8[1]};
assign b8_0_w5 = {b8[0]};
assign b6_0_w7 = {b6[0]};
assign b6_1_w8 = {b6[1]};

PNU_MUX4
     s0 (
      .o1(w0),
      .i4(b8_3_w2),
      .i3(b8_2_w3),
      .i2(b8_1_w4),
      .i1(b8_0_w5),
      .e1(b6_0_w7),
      .e2(b6_1_w8));

endmodule

