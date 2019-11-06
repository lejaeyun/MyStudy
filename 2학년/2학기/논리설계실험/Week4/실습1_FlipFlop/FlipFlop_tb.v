module FlipFlop_tb;

reg CLK;
reg Din;
wire Qout;
reg RST;

FlipFlop
 U0 (
  .CLK(CLK),
  .Din(Din),
  .Qout(Qout),
  .RST(RST));

  initial
  begin
    CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
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
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
  end

  initial
  begin
    Din = 1'b0;
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
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
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
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
  end


endmodule
