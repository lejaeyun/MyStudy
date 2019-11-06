module DecimalToBinary(d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,CHK,Dout);

input d0;
input d1;
input d2;
input d3;
input d4;
input d5;
input d6;
input d7;
input d8;
input d9;
output CHK;
output [3:0] Dout;

wire  w1;
wire  w5;
wire  w7;
wire  w9;
wire  w11;
wire  w8;
wire  w12;
wire  w10;
wire  w19;
wire  w18;
wire  w13;
wire  w20;
wire [3:0] b16;
wire  b16_0;
wire  b16_0_w21;
wire  b16_1;
wire  b16_1_w15;
wire  b16_2;
wire  b16_2_w16;
wire  b16_3;
wire  b16_3_w17;

assign w18 = d0;
assign w11 = d1;
assign w7 = d2;
assign w8 = d3;
assign w5 = d4;
assign w12 = d5;
assign w9 = d6;
assign w10 = d7;
assign w1 = d8;
assign w13 = d9;
assign CHK = w20;
assign Dout = b16;

assign b16[3] = b16_3;
assign b16[2] = b16_2;
assign b16[1] = b16_1;
assign b16[0] = b16_0;

assign b16_0_w21 = {b16[0]};
assign b16_1_w15 = {b16[1]};
assign b16_2_w16 = {b16[2]};
assign b16_3_w17 = {b16[3]};

PNU_OR2
     s0 (
      .i1(w1),
      .i2(w13),
      .o1(b16_3));

PNU_OR4
     s1 (
      .i1(w7),
      .i3(w9),
      .i2(w8),
      .i4(w10),
      .o1(b16_1));

PNU_OR4
     s2 (
      .i1(w5),
      .i3(w9),
      .i2(w12),
      .i4(w10),
      .o1(b16_2));

PNU_OR8
     s3 (
      .i1(w11),
      .i2(w8),
      .i3(w12),
      .i4(w10),
      .i8(w19),
      .i6(w19),
      .i7(w19),
      .i5(w13),
      .o1(b16_0));

PNU_ZERO
     s5 (
      .o1(w19));

PNU_OR4
     s9 (
      .o1(w20),
      .i1(b16_0_w21),
      .i2(b16_1_w15),
      .i3(b16_2_w16),
      .i4(b16_3_w17));

endmodule

