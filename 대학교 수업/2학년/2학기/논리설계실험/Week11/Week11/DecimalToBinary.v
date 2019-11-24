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
wire  w13;
wire [3:0] b17;
wire  w18;
wire  w20;
wire  w22;
wire  b17_0;
wire  b17_0_w21;
wire  b17_1;
wire  b17_1_w15;
wire  b17_2;
wire  b17_2_w16;
wire  b17_3;
wire  b17_3_w17;

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
assign CHK = w22;
assign Dout = b17;

assign b17[3] = b17_3;
assign b17[2] = b17_2;
assign b17[1] = b17_1;
assign b17[0] = b17_0;

assign b17_0_w21 = {b17[0]};
assign b17_1_w15 = {b17[1]};
assign b17_2_w16 = {b17[2]};
assign b17_3_w17 = {b17[3]};

PNU_OR2
     s0 (
      .i1(w1),
      .i2(w13),
      .o1(b17_3));

PNU_OR4
     s1 (
      .i1(w7),
      .i3(w9),
      .i2(w8),
      .i4(w10),
      .o1(b17_1));

PNU_OR4
     s2 (
      .i1(w5),
      .i3(w9),
      .i2(w12),
      .i4(w10),
      .o1(b17_2));

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
      .o1(b17_0));

PNU_ZERO
     s5 (
      .o1(w19));

PNU_OR4
     s9 (
      .i1(b17_0_w21),
      .i2(b17_1_w15),
      .i3(b17_2_w16),
      .i4(b17_3_w17),
      .o1(w20));

PNU_OR2
     s6 (
      .i1(w18),
      .i2(w20),
      .o1(w22));

endmodule

