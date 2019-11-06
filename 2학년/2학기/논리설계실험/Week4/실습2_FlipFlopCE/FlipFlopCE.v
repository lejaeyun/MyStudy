module FlipFlopCE(Ce,Din,CLK,RST,Qout);

input Ce;
input Din;
input CLK;
input RST;
output Qout;

wire  w0;
wire  w1;
wire  w2;
wire  w3;
wire  w4;

assign w3 = Ce;
assign w2 = Din;
assign w1 = CLK;
assign w0 = RST;
assign Qout = w4;

PNU_DFF_Ce
     s0 (
      .reset(w0),
      .clock(w1),
      .D(w2),
      .Ce(w3),
      .Q(w4));

endmodule

