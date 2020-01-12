state
out(0)

state
loop:
    out(0)
    >

>

state

loop:
    put(1)
	loop:
		<
		out(0)
	loop:
		<
		out(1)
     
    state
	<
	out(0)
	>
    
	put(0)
	loop:
		>
		out(1)
	loop:
		>
		out(0)
 
state

>
loop:
	>
	out(1)
	put(1)

<
put(0)
>
state