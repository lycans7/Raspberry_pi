/*while ( 1 )
	{
		/*digitalWrite( DHTPIN, HIGH );
		printf("after high\n");
		digitalWrite( 10, HIGH );
		delay( 1000 );
		printf("after delay\n");
		digitalWrite( DHTPIN, LOW );
		printf("after low\n");
		digitalWrite( 10, LOW );
		delay( 1000 );*/
		read_dht11_dat();
		delay( 1000 ); /* wait 1sec to refresh*/
	}*/