module Training2(Sum,Dec,RST);

output [4:0] Sum;
input [9:0] Dec;
input RST;

wire [3:0] b6;
wire  w10;
wire  w11;
wire [3:0] b15;
wire [3:0] b11;
wire [4:0] b20;
wire  w26;
wire [4:0] b27;
wire  w28;
wire  w29;
wire  w31;
wire [9:0] b32;
wire  w43;
wire  b6_3;
wire  b6_2;
wire  b6_0;
wire  b6_1;
wire [3:0] b15_3to0;
wire  b11_0_w12;
wire  b11_1_w13;
wire  b11_2_w14;
wire  b11_3_w15;
wire  b15_3_w16;
wire  b15_2_w17;
wire  b15_1_w18;
wire  b15_0_w19;
wire  b20_4;
wire  b20_3;
wire  b20_2;
wire  b20_1;
wire  b20_0;
wire  b32_0_w33;
wire  b32_1_w34;
wire  b32_2_w35;
wire  b32_3_w36;
wire  b32_4_w37;
wire  b32_5_w38;
wire  b32_6_w39;
wire  b32_7_w40;
wire  b32_8_w41;
wire  b32_9_w42;

assign Sum = b27;
assign b32 = Dec;
assign w43 = RST;

assign b6[3] = b6_3;
assign b6[2] = b6_2;
assign b6[1] = b6_1;
assign b6[0] = b6_0;
assign b15[3:0] = b15_3to0[3:0];
assign b20[4] = b20_4;
assign b20[3] = b20_3;
assign b20[2] = b20_2;
assign b20[1] = b20_1;
assign b20[0] = b20_0;

assign b11_0_w12 = {b11[0]};
assign b11_1_w13 = {b11[1]};
assign b11_2_w14 = {b11[2]};
assign b11_3_w15 = {b11[3]};
assign b15_3_w16 = {b15[3]};
assign b15_2_w17 = {b15[2]};
assign b15_1_w18 = {b15[1]};
assign b15_0_w19 = {b15[0]};
assign b32_0_w33 = {b32[0]};
assign b32_1_w34 = {b32[1]};
assign b32_2_w35 = {b32[2]};
assign b32_3_w36 = {b32[3]};
assign b32_4_w37 = {b32[4]};
assign b32_5_w38 = {b32[5]};
assign b32_6_w39 = {b32[6]};
assign b32_7_w40 = {b32[7]};
assign b32_8_w41 = {b32[8]};
assign b32_9_w42 = {b32[9]};

FourbitReg
     s0 (
      .CLK(w10),
      .Qout(b11),
      .Din(b15),
      .Ce(w31),
      .RST(w43));

RippleCarryAdder
     s3 (
      .B0(b11_0_w12),
      .B1(b11_1_w13),
      .B2(b11_2_w14),
      .B3(b11_3_w15),
      .A3(b15_3_w16),
      .A2(b15_2_w17),
      .A1(b15_1_w18),
      .A0(b15_0_w19),
      .C4(b20_4),
      .S3(b20_3),
      .S2(b20_2),
      .S1(b20_1),
      .S0(b20_0),
      .C0(w26));

FivebitReg
     s4 (
      .Din(b20),
      .Qout(b27),
      .Ce(w28),
      .CLK(w29),
      .RST(w43));

PNU_ONE
     s5 (
      .o1(w11));

PNU_ONE
     s8 (
      .o1(w10));

FourbitReg
     s1 (
      .Din(b6),
      .CLK(w11),
      .Qout(b15),
      .Ce(w31),
      .RST(w43));

PNU_ZERO
     s9 (
      .o1(w26));

PNU_ONE
     s10 (
      .o1(w28));

PNU_ONE
     s11 (
      .o1(w29));

DecimalToBinaryWithCHK
     s13 (
      .b3(b6_3),
      .b2(b6_2),
      .b0(b6_0),
      .b1(b6_1),
      .CHK(w31),
      .d0(b32_0_w33),
      .d1(b32_1_w34),
      .d2(b32_2_w35),
      .d3(b32_3_w36),
      .d4(b32_4_w37),
      .d5(b32_5_w38),
      .d6(b32_6_w39),
      .d7(b32_7_w40),
      .d8(b32_8_w41),
      .d9(b32_9_w42));

endmodule

