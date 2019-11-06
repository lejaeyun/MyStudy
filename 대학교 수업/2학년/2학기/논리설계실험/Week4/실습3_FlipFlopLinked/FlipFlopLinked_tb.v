module FlipFlopLinked_tb;

reg CLK;
reg Din;
wire Q0;
wire Q1;
wire Q2;
wire Q3;
reg RST;

FlipFlopLinked
 U0 (
  .CLK(CLK),
  .Din(Din),
  .Q0(Q0),
  .Q1(Q1),
  .Q2(Q2),
  .Q3(Q3),
  .RST(RST));
  initial
  begin
    CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
  end

  initial
  begin
    RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
  end

  initial
  begin
    Din = 1'b1;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
  end


endmodule
