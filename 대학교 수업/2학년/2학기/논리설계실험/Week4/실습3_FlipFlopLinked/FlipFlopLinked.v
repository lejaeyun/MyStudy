module FlipFlopLinked(Din,CLK,RST,Q3,Q0,Q1,Q2);

input Din;
input CLK;
input RST;
output Q3;
output Q0;
output Q1;
output Q2;

wire  w3;
wire  w4;
wire  w2;
wire  w8;
wire  w7;
wire  w6;
wire  w9;

assign w3 = Din;
assign w2 = CLK;
assign w4 = RST;
assign Q3 = w9;
assign Q0 = w8;
assign Q1 = w7;
assign Q2 = w6;

PNU_DFF
     s0 (
      .D(w3),
      .reset(w4),
      .clock(w2),
      .Q(w9));

PNU_DFF
     s1 (
      .reset(w4),
      .clock(w2),
      .Q(w6),
      .D(w9));

PNU_DFF
     s2 (
      .reset(w4),
      .clock(w2),
      .Q(w7),
      .D(w6));

PNU_DFF
     s3 (
      .reset(w4),
      .clock(w2),
      .Q(w8),
      .D(w7));

endmodule

