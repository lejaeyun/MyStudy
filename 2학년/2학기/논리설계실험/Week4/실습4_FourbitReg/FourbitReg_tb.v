module FourbitReg_tb;

reg CLK;
reg Ce;
reg [3:0] Din;
wire [3:0] Qout;
reg RST;

FourbitReg
 U0 (
  .CLK(CLK),
  .Ce(Ce),
  .Din(Din),
  .Qout(Qout),
  .RST(RST));
  initial
  begin
    RST = 1'b0;
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
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
  end

  initial
  begin
    Din = 4'b0000;
    #100 Din = 4'b1111;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b1111;
    #100 Din = 4'b0000;
    #100 Din = 4'b0101;
    #100 Din = 4'b0000;
    #100 Din = 4'b1010;
    #100 Din = 4'b0000;
    #100 Din = 4'b0001;
    #100 Din = 4'b0000;
    #100 Din = 4'b0001;
    #100 Din = 4'b0000;
    #100 Din = 4'b1111;
    #100 Din = 4'b0000;
    #100 Din = 4'b0010;
    #100 Din = 4'b0000;
    #100 Din = 4'b1000;
    #100 Din = 4'b0000;
    #100 Din = 4'b1010;
    #100 Din = 4'b0000;
    #100 Din = 4'b0011;
    #100 Din = 4'b0000;
    #100 Din = 4'b0101;
    #100 Din = 4'b0000;
    #100 Din = 4'b1110;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b0000;
    #100 Din = 4'b1110;
    #100 Din = 4'b0000;
    #100 Din = 4'b0001;
    #100 Din = 4'b0000;
    #100 Din = 4'b1001;
    #100 Din = 4'b0000;
    #100 Din = 4'b0101;
    #100 Din = 4'b0000;
  end

  initial
  begin
    Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b1;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
    #100 Ce = 1'b0;
  end

  initial
  begin
    CLK = 1'b0;
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
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
  end



endmodule
