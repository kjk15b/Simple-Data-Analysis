/*
Carolina Ramirez
MD Anderson
Kolby Kiesling
ACU Nuclear Physics Research
*/

void curtis_sim() {
	TH1F *h1 = new TH1F("h1", "NUDT5 Expression Among Negative Samples; NUDT5; Samples ()", 125, -2, 10);
	TH1F *h2 = new TH1F("h2", "NUDT5 Expression Among Positive Samples; NUDT5; Samples ()", 125, -2, 10);
	TH2F *h3 = new TH2F("h3", "NUDT5 Expression Among ER Samples; Curtis Negative; Curtis Positve", 125, -2, 10, 125, -2, 10);
	
	TRandom3 rndgen;
	
	TFile *f = new TFile("curtis_simulation.root", "RECREATE");
	
	for(int i=0; i<1000000; i++){
		h1->Fill(gRandom->Landau(3.903, 0.4283)); // Curtis Negative
		h2->Fill(gRandom->Gaus(3.609, 0.4085));
		h3->Fill(gRandom->Landau(3.903, 0.4283), gRandom->Gaus(3.609, 0.4085));
	}
	
	h1->Write();
	h2->Write();
	h3->Write();
	
	f->Close();
	
	return 0;

}