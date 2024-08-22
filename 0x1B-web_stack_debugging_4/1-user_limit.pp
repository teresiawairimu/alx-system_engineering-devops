# fix hard and soft file limits

exec { 'Fix hard file limit':
  command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path     => 'usr/local/bin/:/bin/',
  provider => 'shell'
}

exec { 'fix soft file limit':
  command  => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}
