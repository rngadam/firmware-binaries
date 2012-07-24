		if((gSYS_ID == 0x1)&&(gSYS_ID_FLAG == 0xEA68)){
			grid_func_led_set(0, 0, 0x60, 0x15);
			grid_func_led_set(1, 0, 0x60, 0x15);
			grid_func_led_set(2, 0x60, 0, 0x15);
			grid_func_led_set(3, 0x60, 0, 0x15);
			
			grid_shield_a_lo_en();
			grid_shield_a_hi_en();
			grid_shield_b_lo_en();
			grid_shield_b_hi_en();
			grid_shield_a_pwr_en();
			grid_shield_b_pwr_en();

			for(i=0; i<26; i++) {
				GRID_PWM(i)->PWM_RESET = 0;
				GRID_PWM(i)->PWM_GATE = 0x0000FFFF;
			}
			
			for(i=0; i<26; i++){
				for(j=0; j<=0x8000; j = j+0x200){
					if(i >= 2) GRID_PWM((U8)(i-2))->PWM_DTYC = j/128;
					if(i >= 1) GRID_PWM((U8)(i-1))->PWM_DTYC = j/8;
					GRID_PWM(i)->PWM_DTYC = j;
					if(i <= 25) GRID_PWM((U8)(i+1))->PWM_DTYC = j/8;
					if(i <= 24) GRID_PWM((U8)(i+2))->PWM_DTYC = j/128;				
					Delay_ms(20);
				}
				
				Delay_ms(50);
				
				for(j=0; j<=0x8000; j = j+0x200){
					if(i >= 2) GRID_PWM((U8)(i-2))->PWM_DTYC = (0x8000 - j)/128;
					if(i >= 1) GRID_PWM((U8)(i-1))->PWM_DTYC = (0x8000 - j)/8;
					GRID_PWM(i)->PWM_DTYC = 0x8000 - j;
					if(i <= 25) GRID_PWM((U8)(i+1))->PWM_DTYC = (0x8000 - j)/8;
					if(i <= 24) GRID_PWM((U8)(i+2))->PWM_DTYC = (0x8000 - j)/128;
					Delay_ms(10);
				}
				
				Delay_ms(50);
			}
			
 			GRID_PIO26_SLOT_A->PIO_DOE = (0xFFFFFFFF);
 			GRID_PIO26_SLOT_B->PIO_DOE = (0xFFFFFFFF);

 			for(i=0; i<4; i++)
 			{
 				GRID_PIO26_SLOT_A->PIO_DOUT[i] = (0x0);
 				Delay_ms(200);
 				GRID_PIO26_SLOT_A->PIO_DOUT[i] = (0xFF);
 			}

 			for(i=0; i<26; i++)
 			{
 				GRID_PIO26_SLOT_A->PIO_IO[i] = 0;
 				Delay_ms(50);
 				GRID_PIO26_SLOT_A->PIO_IO[i] = 1;
 			}
		}