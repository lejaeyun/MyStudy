module week03_training2(A,B,Sum);

input [9:0] A;
input [9:0] B;
output [4:0] Sum;

wire  w6;
wire  w7;
wire  w8;
wire  w9;
wire [4:0] b10;
wire  w16;
wire [9:0] b0;
wire [9:0] b36;
wire  w38;
wire  w39;
wire  w40;
wire  w41;
wire  b10_0;
wire  b10_4;
wire  b10_3;
wire  b10_2;
wire  b10_1;
wire  b0_9_w17;
wire  b0_8_w18;
wire  b0_7_w19;
wire  b0_6_w20;
wire  b0_5_w21;
wire  b0_4_w22;
wire  b0_3_w23;
wire  b0_2_w24;
wire  b0_1_w25;
wire  b0_0_w26;
wire  b36_0_w28;
wire  b36_1_w29;
wire  b36_2_w30;
wire  b36_3_w31;
wire  b36_5_w33;
wire  b36_6_w34;
wire  b36_7_w35;
wire  b36_8_w36;
wire  b36_9_w37;
wire  b36_4_w42;

assign b0 = A;
assign b36 = B;
assign Sum = b10;

assign b10[4] = b10_4;
assign b10[3] = b10_3;
assign b10[2] = b10_2;
assign b10[1] = b10_1;
assign b10[0] = b10_0;

assign b0_9_w17 = {b0[9]};
assign b0_8_w18 = {b0[8]};
assign b0_7_w19 = {b0[7]};
assign b0_6_w20 = {b0[6]};
assign b0_5_w21 = {b0[5]};
assign b0_4_w22 = {b0[4]};
assign b0_3_w23 = {b0[3]};
assign b0_2_w24 = {b0[2]};
assign b0_1_w25 = {b0[1]};
assign b0_0_w26 = {b0[0]};
assign b36_0_w28 = {b36[0]};
assign b36_1_w29 = {b36[1]};
assign b36_2_w30 = {b36[2]};
assign b36_3_w31 = {b36[3]};
assign b36_5_w33 = {b36[5]};
assign b36_6_w34 = {b36[6]};
assign b36_7_w35 = {b36[7]};
assign b36_8_w36 = {b36[8]};
assign b36_9_w37 = {b36[9]};
assign b36_4_w42 = {b36[4]};

decimal_to_binary
     s1 (
      .d0(b36_0_w28),
      .d1(b36_1_w29),
      .d2(b36_2_w30),
      .d3(b36_3_w31),
      .d5(b36_5_w33),
      .d6(b36_6_w34),
      .d7(b36_7_w35),
      .d8(b36_8_w36),
      .d9(b36_9_w37),
      .b0(w38),
      .b1(w39),
      .b2(w40),
      .b3(w41),
      .d4(b36_4_w42));

Ripple_Carry_Adder
     s2 (
      .A0(w6),
      .A1(w7),
      .A2(w8),
      .A3(w9),
      .S0(b10_0),
      .S4(b10_4),
      .S3(b10_3),
      .S2(b10_2),
      .S1(b10_1),
      .C0(w16),
      .B0(w38),
      .B1(w39),
      .B2(w40),
      .B3(w41));

PNU_ZERO
     s3 (
      .o1(w16));

decimal_to_binary
     s0 (
      .b0(w6),
      .b1(w7),
      .b2(w8),
      .b3(w9),
      .d9(b0_9_w17),
      .d8(b0_8_w18),
      .d7(b0_7_w19),
      .d6(b0_6_w20),
      .d5(b0_5_w21),
      .d4(b0_4_w22),
      .d3(b0_3_w23),
      .d2(b0_2_w24),
      .d1(b0_1_w25),
      .d0(b0_0_w26));

endmodule

