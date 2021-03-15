def Results(counter,elapsed,Netloc,Path):
	#Output of the final result of the program.
	print(

		f'\n\n\033[38;5;201mNumber of links found: \033[38;5;226m{counter}\033[0m',
		f'\n\n\033[38;5;201mTime (seconds):\033[38;5;226m %.4f \033[0m' % (elapsed),
		f'\n\n\033[38;5;201mLink URL Root: \033[38;5;226m\033[4m{Netloc}\033[0m',
		f'\n\n\033[38;5;201mPath file site-map: \033[38;5;123m\n\n\033[4m{Path}\033[0m\n'

		)