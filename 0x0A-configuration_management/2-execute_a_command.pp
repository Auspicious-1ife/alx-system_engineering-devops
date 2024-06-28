# This Puppet manifest kills a process named killmenow using pkill
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}

