#!/usr/bin/perl

#usage: perl script.pl fastainput blocksize(bp) > STDOUT/FILE
#takes a gff and calculates density per block for a given list of feature type (i.e. gene density per 10000bp)

open(IN, '<', @ARGV[0]);

$hash = undef;
#hash{seq}->{start/stop midpoint}
$fasta = do {local $/; <IN>};
@fasta = split(/>/, $fasta);
%lenhash = undef;
foreach $fasrec (@fasta) {
	unless ($fasrec eq undef) {
		@data = split(/\n/, $fasrec, 2);
		@data[1] =~ s/\n|\s//sgi;
		$length = length(@data[1]);
		for ($i = 1; $i < $length; $i += @ARGV[1]) {
			$min = $i - (@ARGV[1] / 2);
			$max = $i + (@ARGV[1] / 2);
			if ($min < 1) {
				$min = 1;
			}
			if ($max > $length) {
				$max = $length;
			}
			$sub = substr(@data[1], ($min -1), ($max - $min + 1));
			$sub =~ s/Nn//sgi;
			#$sublen = length($sub);
			$temp = ($sub =~ tr/GCATgcat/GCATgcat/);
			if ($temp == 0) {
				$gc = 0;
			}
			else {
				$gc = ($sub =~ tr/GCgc/GCgc/) / ($sub =~ tr/GCATgcat/GCATgcat/) * 100;
			}
			print "@data[0]\t$min\t$max\t$gc\n";
		}
		
	}
}

