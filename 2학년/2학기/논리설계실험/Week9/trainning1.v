module trainning1(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,RST,CLK,LV,com8,com1,com2,com3,com4,com5,com6,com7,a,c,d,f,g,e,b);

input p0;
input p1;
input p2;
input p3;
input p4;
input p5;
input p6;
input p7;
input p8;
input p9;
input RST;
input CLK;
input LV;
output com8;
output com1;
output com2;
output com3;
output com4;
output com5;
output com6;
output com7;
output a;
output c;
output d;
output f;
output g;
output e;
output b;

wire  w6;
wire  w7;
wire  w8;
wire  w9;
wire  w10;
wire  w11;
wire  w12;
wire  w13;
wire  w14;
wire  w15;
wire  w16;
wire  w18;
wire  w19;
wire  w20;
wire  w23;
wire  w26;
wire  w27;
wire [3:0] b28;
wire [3:0] b26;
wire  w28;
wire [3:0] b27;
wire  w29;
wire  w32;
wire  w33;
wire  w34;
wire  w35;
wire  w36;
wire  w37;
wire  w38;
wire  w39;
wire  w40;
wire  w42;
wire  w43;
wire  w41;
wire  w44;
wire  w45;
wire  w46;
wire  w47;
wire  w48;
wire  w50;
wire  w49;
wire  w51;

assign w7 = p0;
assign w8 = p1;
assign w9 = p2;
assign w10 = p3;
assign w11 = p4;
assign w12 = p5;
assign w13 = p6;
assign w14 = p7;
assign w15 = p8;
assign w16 = p9;
assign w51 = RST;
assign w39 = CLK;
assign w6 = LV;
assign com8 = w18;
assign com1 = w27;
assign com2 = w27;
assign com3 = w27;
assign com4 = w27;
assign com5 = w27;
assign com6 = w27;
assign com7 = w19;
assign a = w20;
assign c = w23;
assign d = w41;
assign f = w40;
assign g = w26;
assign e = w43;
assign b = w42;

BinaryToSegment
     s0 (
      .Din(b26),
      .segg(w34),
      .segf(w35),
      .sege(w37),
      .segd(w44),
      .segc(w45),
      .segb(w46),
      .sega(w48));

DecimalToBinary
     s1 (
      .d0(w7),
      .d1(w8),
      .d2(w9),
      .d3(w10),
      .d4(w11),
      .d5(w12),
      .d6(w13),
      .d7(w14),
      .d8(w15),
      .d9(w16),
      .Dout(b28),
      .CHK(w28));

LTP
     s2 (
      .Level(w6),
      .Pulse(w29),
      .clk(w39),
      .rst(w51));

PNU_NOT
     s5 (
      .o1(w18),
      .i1(w39));

PNU_ONE
     s6 (
      .o1(w27));

PNU_NOT
     s7 (
      .i1(w18),
      .o1(w19));

FourbitReg
     s8 (
      .Din(b28),
      .Qout(b26),
      .Ce(w28),
      .CLK(w29),
      .RST(w51));

FourbitReg
     s9 (
      .Din(b26),
      .Ce(w28),
      .Qout(b27),
      .CLK(w29),
      .RST(w51));

BinaryToSegment
     s10 (
      .Din(b27),
      .sega(w32),
      .segg(w33),
      .segf(w36),
      .sege(w38),
      .segb(w47),
      .segd(w50),
      .segc(w49));

PNU_MUX2
     s11 (
      .o1(w20),
      .i1(w32),
      .e1(w39),
      .i2(w48));

PNU_MUX2
     s12 (
      .e1(w39),
      .o1(w42),
      .i2(w46),
      .i1(w47));

PNU_MUX2
     s13 (
      .o1(w23),
      .e1(w39),
      .i2(w45),
      .i1(w49));

PNU_MUX2
     s14 (
      .e1(w39),
      .o1(w41),
      .i2(w44),
      .i1(w50));

PNU_MUX2
     s15 (
      .i1(w37),
      .i2(w38),
      .e1(w39),
      .o1(w43));

PNU_MUX2
     s16 (
      .i2(w35),
      .i1(w36),
      .e1(w39),
      .o1(w40));

PNU_MUX2
     s17 (
      .o1(w26),
      .i1(w33),
      .i2(w34),
      .e1(w39));

endmodule

