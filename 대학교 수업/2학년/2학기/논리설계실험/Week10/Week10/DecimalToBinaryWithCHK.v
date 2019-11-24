module DecimalToBinaryWithCHK(d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,b3,b2,b1,b0,CHK);

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
output b3;
output b2;
output b1;
output b0;
output CHK;

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
wire  w21;
wire  w15;
wire  w16;
wire  w17;

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
assign b3 = w17;
assign b2 = w16;
assign b1 = w15;
assign b0 = w21;
assign CHK = w20;

PNU_OR2
     s0 (
      .i1(w1),
      .i2(w13),
      .o1(w17));

PNU_OR4
     s1 (
      .i1(w7),
      .i3(w9),
      .i2(w8),
      .i4(w10),
      .o1(w15));

PNU_OR4
     s2 (
      .i1(w5),
      .i3(w9),
      .i2(w12),
      .i4(w10),
      .o1(w16));

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
      .o1(w21));

PNU_ZERO
     s5 (
      .o1(w19));

PNU_OR4
     s9 (
      .o1(w20),
      .i1(w21),
      .i2(w15),
      .i3(w16),
      .i4(w17));

endmodule

