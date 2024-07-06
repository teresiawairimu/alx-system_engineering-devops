# kills a process 'killmenow'
exec {'kill `killmenow` process':
command => '/usr/bin/pkill -9 -f killmenow',
onlyif  => '/usr/bin/pgrep -f killmenow'
}
