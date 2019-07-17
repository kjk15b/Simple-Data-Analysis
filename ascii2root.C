#include "Riostream.h"
#include "TH2.h"
#include <iostream>
using namespace std;

void file2root(const char* __file__)
{
	std::string::size_type sz;
	/* Finding the file and creating the ROOT file */
	TString dir = gSystem->UnixPathName(__file__);
	dir.ReplaceAll("ascii2root.C","");
	dir.ReplaceAll("/./","/");

	ifstream in;
	in.open(Form(__file__, dir.Data()));

	Float_t curtis_pos_NUDT, curtis_neg_NUDT, curtis_nor_NUDT, vande_pos_NUDT, vande_neg_NUDT, gluck_pos_NUDT, gluck_neg_NUDT, gluck_nor_NUDT, chin_pos_NUDT, chin_neg_NUDT, a, b, tcga_pos_NUDT, tcga_neg_NUDT, tcga_nor_NUDT;
	string s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13;
	Int_t nlines = 0;
	
	TFile *f = new TFile("total_cancer_data.root", "RECREATE");
	
	TH1F *h1 = new TH1F("h1", "Curtis Positive NUDT5", 125, -2, 10);
	TH1F *h2 = new TH1F("h2", "Curtis Negative NUDT5", 125, -2, 10);
	TH1F *h3 = new TH1F("h3", "Curtis Normal NUDT5", 125, -2, 10);
	TH1F *h4 = new TH1F("h4", "VandeVijver Positive NUDT5", 125, -2, 10);
	TH1F *h5 = new TH1F("h5", "VandeVijver Negative NUDT5", 125, -2, 10);
	TH1F *h6 = new TH1F("h6", "Gluck Positive NUDT5", 125, -2, 10);
	TH1F *h7 = new TH1F("h7", "Gluck Negative NUDT5", 125, -2, 10);
	TH1F *h8 = new TH1F("h8", "Gluck Normal NUDT5", 125, -2, 10);
	TH1F *h9 = new TH1F("h9", "Chin Positive NUDT5", 125, -2, 10);
	TH1F *h10 = new TH1F("h10", "Chin Negative NUDT5", 125, -2, 10);
	TH1F *h18 = new TH1F("h18", "TCGA Positive NUDT5", 125, -2, 10);
	TH1F *h19 = new TH1F("h19", "TCGA Negative NUDT5", 125, -2, 10);
	TH1F *h20 = new TH1F("h20", "TCGA Normal NUDT5", 125, -2, 10);
	//TH2F *h2 = new TH2F("h2", "Voltage Response; Waveform(V); Piezo (V)", 1000, 0, 2, 1000, 0.04, 0.1);
	TH2F *h11 = new TH2F("h11", "NUDT5 Expression; Curtis Negative; VandeVijver Negative", 75, -2, 10, 75, -2, 10);
	TH2F *h12 = new TH2F("h12", "NUDT5 Expression; Curtis Negative; Gluck Negative", 75, -2, 10, 75, -2, 10);
	TH2F *h13 = new TH2F("h13", "NUDT5 Expression; Curtis Negative; Chin Negative", 75, -2, 10, 75, -2, 10);
	TH2F *h14 = new TH2F("h14", "NUDT5 Expression; Curtis Negative; Curtis Positive", 75, -2, 10, 75, -2, 10);
	TH2F *h15 = new TH2F("h15", "NUDT5 Expression; Gluck Negative; Chin Negative", 75, -2, 10, 75, -2, 10);
	TH2F *h16 = new TH2F("h16", "NUDT5 Expression; Gluck Negative; Gluck Positive", 75, -2, 10, 75, -2, 10);
	TH2F *h17 = new TH2F("h17", "NUDT5 Expression; Chin Negative; Chin Positive", 75, -2, 10, 75, -2, 10);
	TH2F *h21 = new TH2F("h21", "NUDT5 Expression; TCGA Negative; TCGA Positive", 75, -2, 10, 75, -2, 10);
	TH2F *h22 = new TH2F("h22", "NUDT5 Expression; Curtis Negative; TCGA Negative", 75, -2, 10, 75, -2, 10);
	/* NTuple handles three columns of data */
	//TNtuple *ntuple = new TNtuple("Cancer Data", "Summer 2019 Data", "a:b:c:d:e:f:g:h:i:j");

	while(1)
	{
		in >> s1 >> s2 >> s3 >> s4 >> s5 >> s6 >> s7 >> s8 >> s9 >> s10 >> s11 >> s12 >> s13;
		//printf(in.readline());
		if(!in.good()) break;
		/* skip the first two lines that are just comments */
		if(nlines > -1)
		{
			curtis_pos_NUDT = std::stof (s1, &sz);
			curtis_neg_NUDT = std::stof (s2, &sz);
			curtis_nor_NUDT = std::stof (s3, &sz);
			vande_pos_NUDT = std::stof (s4, &sz);
			vande_neg_NUDT = std::stof (s5, &sz);
			gluck_pos_NUDT = std::stof (s6, &sz);
			gluck_neg_NUDT = std::stof (s7, &sz);
			gluck_nor_NUDT = std::stof (s8, &sz);
			chin_pos_NUDT = std::stof (s9, &sz);
			chin_neg_NUDT = std::stof (s10, &sz);
			tcga_pos_NUDT = std::stof (s11, &sz);
			tcga_neg_NUDT = std::stof (s12, &sz);
			tcga_nor_NUDT = std::stof (s13, &sz);
			if(nlines < 8) printf("curtis_pos_NUDT=%8f\tcurtis_neg_NUDT=%8f\tcurtis_nor_NUDT=%8f\nvande_pos_NUDT=%8f\tvande_neg_NUDT=%8f\tgluck_pos_NUDT=%8f\ntcga_pos_NUDT=%8f", curtis_pos_NUDT, curtis_neg_NUDT, curtis_nor_NUDT, vande_pos_NUDT, vande_neg_NUDT, gluck_pos_NUDT,tcga_pos_NUDT);
			h1->Fill(curtis_pos_NUDT);
			h2->Fill(curtis_neg_NUDT);
			h3->Fill(curtis_nor_NUDT);
			h4->Fill(vande_pos_NUDT);
			h5->Fill(vande_neg_NUDT);
			h6->Fill(gluck_pos_NUDT);
			h7->Fill(gluck_neg_NUDT);
			h8->Fill(gluck_nor_NUDT);
			h9->Fill(chin_pos_NUDT);
			h10->Fill(chin_neg_NUDT);
			h11->Fill(curtis_neg_NUDT, vande_neg_NUDT);
			h12->Fill(curtis_neg_NUDT, gluck_neg_NUDT);
			h13->Fill(curtis_neg_NUDT, chin_neg_NUDT);
			h14->Fill(curtis_neg_NUDT, curtis_pos_NUDT);
			h15->Fill(gluck_neg_NUDT, chin_neg_NUDT);
			h16->Fill(gluck_neg_NUDT, gluck_pos_NUDT);
			h17->Fill(chin_neg_NUDT, chin_pos_NUDT);
			h18->Fill(tcga_pos_NUDT);
			h19->Fill(tcga_neg_NUDT);
			h20->Fill(tcga_nor_NUDT);
			h21->Fill(tcga_neg_NUDT, tcga_pos_NUDT);
			h22->Fill(curtis_neg_NUDT, tcga_neg_NUDT);
			a = gluck_neg_NUDT / curtis_neg_NUDT;
			b = chin_neg_NUDT / curtis_neg_NUDT;
			h15->Fill(a, b);
			//ntuple->Fill(curtis_pos_NUDT, curtis_pos_NUDT, curtis_nor_NUDT, vande_pos_NUDT, vande_neg_NUDT, gluck_pos_NUDT, gluck_neg_NUDT, gluck_nor_NUDT, chin_pos_NUDT, chin_neg_NUDT);
		}
		nlines++;
	}

	printf(" Found %d points\n", nlines);
	in.close();
	f->Write();
}

