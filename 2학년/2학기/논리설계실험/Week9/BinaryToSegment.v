module BinaryToSegment(Din,sega,segb,segc,segd,sege,segf,segg);

input [3:0] Din;
output sega;
output segb;
output segc;
output segd;
output sege;
output segf;
output segg;

wire [3:0] b0;
wire  w10;
wire  w14;
wire  w19;
wire  w21;
wire  w22;
wire  w24;
wire  w20;
wire  w30;
wire  w31;
wire  w34;
wire  w35;
wire  w36;
wire  w27;
wire  w37;
wire  w38;
wire  w39;
wire  w29;
wire  w32;
wire  w28;
wire  w40;
wire  w41;
wire  w42;
wire  b0_1_w26;
wire  b0_2_w23;
wire  b0_0_w33;
wire  b0_3_w25;

assign b0 = Din;
assign sega = w14;
assign segb = w21;
assign segc = w22;
assign segd = w35;
assign sege = w36;
assign segf = w37;
assign segg = w40;

assign b0_3_w25 = {b0[3]};// Din A
assign b0_2_w23 = {b0[2]};// Din B
assign b0_1_w26 = {b0[1]};// Din C
assign b0_0_w33 = {b0[0]};// Din D

PNU_NOT
     s0 (
      .o1(w31),
      .i1(b0_0_w33));
// w31 Not D

PNU_NOT
     s1 (
      .o1(w20),
      .i1(b0_2_w23));
//w20 Not B

PNU_NOT
     s2 (
      .i1(b0_3_w25),
      .o1());
//? = not A  nouse

PNU_NOT
     s3 (
      .i1(b0_1_w26),
      .o1(w30));
// w30 Not C

PNU_AND2
     s4 (
      .o1(w10),
      .i1(b0_2_w23),
      .i2(b0_0_w33));
// w10 = BD

PNU_AND2
     s5 (
      .i2(w20),
      .i1(w31),
      .o1(w27));
// w27 = B/D/

PNU_OR4
     s6 (
      .i1(w10),
      .o1(w14),
      .i2(b0_1_w26),
      .i4(w27),
      .i3(b0_3_w25));
// A + 

PNU_AND2
     s7 (
      .o1(w19),
      .i1(w30),
      .i2(w31));
//W19 = C/D/

PNU_AND2
     s8 (
      .i1(b0_1_w26),
      .i2(b0_0_w33),
      .o1(w39));
//W39 =CD

PNU_OR4
     s9 (
      .i1(w19),
      .o1(w21),
      .i2(w20),
      .i4(w39),
      .i3(w42));

PNU_OR4
     s10 (
      .o1(w22),
      .i2(w30),
      .i1(b0_2_w23),
      .i3(b0_0_w33),
      .i4(w41));

PNU_OR4
     s11 (
      .o1(w24),
      .i3(w34),
      .i1(w27),
      .i4(w29),
      .i2(w28));

PNU_OR2
     s12 (
      .i1(w24),
      .o1(w35),
      .i2(b0_3_w25));

PNU_AND2
     s13 (
      .i1(b0_1_w26),
      .i2(w31),
      .o1(w28));

PNU_AND2
     s14 (
      .i1(w20),
      .i2(b0_1_w26),
      .o1(w29));

PNU_AND2
     s15 (
      .i2(w30),
      .i1(b0_2_w23),
      .o1(w32));

PNU_AND2
     s16 (
      .i1(b0_2_w23),
      .i2(w31),
      .o1(w38));

PNU_AND2
     s17 (
      .i1(b0_0_w33),
      .o1(w34),
      .i2(w32));

PNU_OR2
     s18 (
      .o1(w36),
      .i2(w27),
      .i1(w28));

PNU_OR4
     s19 (
      .o1(w37),
      .i2(w38),
      .i1(w39),
      .i4(b0_3_w25),
      .i3(w32));

PNU_OR4
     s20 (
      .i4(b0_3_w25),
      .i3(w29),
      .i2(w32),
      .i1(w28),
      .o1(w40));

PNU_ZERO
     s21 (
      .o1(w41));

PNU_ZERO
     s22 (
      .o1(w42));

endmodule

