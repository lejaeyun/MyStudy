module HundredCounter(clk,rst,CNT10,CNT100);

input clk;
input rst;
output [3:0] CNT10;
output [3:0] CNT100;

wire  w3;
wire  w10;
wire  w11;
wire  w12;
wire  w13;
wire  w14;
wire  w16;
wire  w17;
wire  w18;
wire  w19;
wire  w20;
wire  w21;
wire  w27;
wire  w28;
wire  w26;
wire  w29;
wire [3:0] b25;
wire  w32;
wire  w33;
wire  w34;
wire  w35;
wire  w36;
wire  w37;
wire  w38;
wire  w39;
wire  w40;
wire  w41;
wire  w42;
wire  w43;
wire  w44;
wire  w45;
wire  w46;
wire [3:0] b39;
wire  w57;
wire  w58;
wire  w59;
wire  w60;
wire  w55;
wire  w51;
wire  b39_3;
wire  b39_3_w47;
wire  b39_2;
wire  b39_2_w48;
wire  b39_1;
wire  b39_1_w49;
wire  b39_0;
wire  b39_0_w50;
wire  b25_0;
wire  b25_0_w52;
wire  b25_1;
wire  b25_1_w53;
wire  b25_2;
wire  b25_2_w56;
wire  b25_3;
wire  b25_3_w54;

assign w3 = clk;
assign w51 = rst;
assign CNT10 = b25;
assign CNT100 = b39;

assign b25[3] = b25_3;
assign b25[2] = b25_2;
assign b25[1] = b25_1;
assign b25[0] = b25_0;
assign b39[3] = b39_3;
assign b39[2] = b39_2;
assign b39[1] = b39_1;
assign b39[0] = b39_0;

assign b39_3_w47 = {b39[3]};
assign b39_2_w48 = {b39[2]};
assign b39_1_w49 = {b39[1]};
assign b39_0_w50 = {b39[0]};
assign b25_0_w52 = {b25[0]};
assign b25_1_w53 = {b25[1]};
assign b25_2_w56 = {b25[2]};
assign b25_3_w54 = {b25[3]};

PNU_DFF
     s0 (
      .clock(w3),
      .Q(w29),
      .D(b25_0_w52),
      .reset(w51));

PNU_DFF
     s1 (
      .clock(w3),
      .Q(w28),
      .D(b25_1_w53),
      .reset(w51));

PNU_DFF
     s2 (
      .clock(w3),
      .Q(w27),
      .D(b25_2_w56),
      .reset(w51));

PNU_DFF
     s3 (
      .clock(w3),
      .Q(w26),
      .D(b25_3_w54),
      .reset(w51));

PNU_AND2
     s4 (
      .i2(w10),
      .o1(w21),
      .i1(w26));

PNU_AND3
     s5 (
      .o1(w20),
      .i1(w27),
      .i2(w28),
      .i3(w29));

PNU_AND2
     s6 (
      .i2(w11),
      .o1(w19),
      .i1(w27));

PNU_AND2
     s7 (
      .i2(w12),
      .o1(w18),
      .i1(w27));

PNU_AND3
     s8 (
      .i1(w13),
      .o1(w17),
      .i2(w28),
      .i3(w29));

PNU_XOR2
     s9 (
      .o1(w16),
      .i1(w28),
      .i2(w29));

PNU_AND2
     s10 (
      .i2(w14),
      .i1(w16),
      .o1(b25_1));

PNU_NOT
     s11 (
      .i1(w29),
      .o1(b25_0));

PNU_NOT
     s12 (
      .o1(w14),
      .i1(w26));

PNU_NOT
     s13 (
      .o1(w13),
      .i1(w27));

PNU_NOT
     s14 (
      .o1(w12),
      .i1(w29));

PNU_NOT
     s15 (
      .o1(w11),
      .i1(w28));

PNU_NOT
     s16 (
      .o1(w10),
      .i1(w29));

PNU_OR2
     s17 (
      .i2(w20),
      .i1(w21),
      .o1(b25_3));

PNU_OR3
     s18 (
      .i3(w17),
      .i2(w18),
      .i1(w19),
      .o1(b25_2));

PNU_DFF
     s19 (
      .Q(w46),
      .D(b39_0_w50),
      .clock(w55),
      .reset(w51));

PNU_DFF
     s20 (
      .Q(w44),
      .D(b39_1_w49),
      .clock(w55),
      .reset(w51));

PNU_DFF
     s21 (
      .Q(w43),
      .D(b39_2_w48),
      .clock(w55),
      .reset(w51));

PNU_DFF
     s22 (
      .Q(w45),
      .D(b39_3_w47),
      .clock(w55),
      .reset(w51));

PNU_AND2
     s23 (
      .i2(w32),
      .o1(w42),
      .i1(w45));

PNU_AND3
     s24 (
      .o1(w41),
      .i1(w43),
      .i2(w44),
      .i3(w46));

PNU_AND2
     s25 (
      .i2(w33),
      .o1(w40),
      .i1(w43));

PNU_AND2
     s26 (
      .i2(w34),
      .o1(w39),
      .i1(w43));

PNU_AND3
     s27 (
      .i1(w35),
      .o1(w38),
      .i2(w44),
      .i3(w46));

PNU_XOR2
     s28 (
      .o1(w37),
      .i1(w44),
      .i2(w46));

PNU_AND2
     s29 (
      .i2(w36),
      .i1(w37),
      .o1(b39_1));

PNU_NOT
     s30 (
      .i1(w46),
      .o1(b39_0));

PNU_NOT
     s31 (
      .o1(w36),
      .i1(w45));

PNU_NOT
     s32 (
      .o1(w35),
      .i1(w43));

PNU_NOT
     s33 (
      .o1(w34),
      .i1(w46));

PNU_NOT
     s34 (
      .o1(w33),
      .i1(w44));

PNU_NOT
     s35 (
      .o1(w32),
      .i1(w46));

PNU_OR2
     s36 (
      .i2(w41),
      .i1(w42),
      .o1(b39_3));

PNU_OR3
     s37 (
      .i3(w38),
      .i2(w39),
      .i1(w40),
      .o1(b39_2));

PNU_AND4
     s38 (
      .i2(w57),
      .i1(w58),
      .i3(w59),
      .i4(w60),
      .o1(w55));

PNU_NOT
     s39 (
      .i1(b25_0_w52),
      .o1(w58));

PNU_NOT
     s40 (
      .i1(b25_1_w53),
      .o1(w57));

PNU_NOT
     s41 (
      .i1(b25_2_w56),
      .o1(w59));

PNU_NOT
     s42 (
      .i1(b25_3_w54),
      .o1(w60));

endmodule

