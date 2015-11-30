function rmNoise(inputFile, outputFile)
	
	im = imread(inputFile);
	im(im>200) = 255;
	imwrite(im, outputFile);

end

