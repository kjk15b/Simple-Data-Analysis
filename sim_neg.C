/* 
Carolina Ramirez
MD Anderson
Kolby Kiesling
ACU Nuclear Physics Research Group
June 18 2019
---------------------------------
This program estimates the expected NUDT5 expression given
the best fits from data sets.

*/
void sim_expr(){
	TH1F *h1 = new TH1F("h1", "NUDT5 Expression Among Negative Samples; NUDT5; Samples ()", 125, -2, 10);
	TH1F *h2 = new TH1F("h2", "NUDT5 Expression Among Negative Samples; NUDT5; Samples ()", 125, -2, 10);
	TH1F *h3 = new TH1F("h3", "NUDT5 Expression Among Negative Samples; NUDT5; Samples ()", 125, -2, 10);
	TH1F *h4 = new TH1F("h4", "NUDT5 Expression Among Negative Samples; NUDT5; Samples ()", 125, -2, 10);
	//auto c1 = new TCanvas();
	
	TRandom3 rndgen;
	
	Float_t curtis, vande, gluck, chin;
	
	for(int i=0; i<100000000; i++)
	{
		h1->Fill(gRandom->Landau(3.903, 0.4283)); // estimated MPV from fitted data (CURTIS)
		h2->Fill(gRandom->Gaus(2.626, 0.09182)); // VANDEVIJVER
		h3->Fill(gRandom->Landau(-0.5821, 0.585)); // GLUCK
		h4->Fill(gRandom->Landau(0.125, 0.0875)); // estimated
	}
	
	TFile *f = new TFile("sim_data.root", "RECREATE");
	h1->Write();
	h2->Write();
	h3->Write();
	h4->Write();
	/*
	TLegend leg(.1,.7,.3,.9,"NUDT5 Negative Expression");
	leg.AddEntry(h1, "Curtis");
	leg.AddEntry(h2, "VandeVijver");
	leg.AddEntry(h3, "Gluck");
	leg.AddEntry(h4, "Chin");
	
	h1->Draw();
	leg->DrawClone("Same");
	*/
	f->Close();
	return 0;
}