%define upstream_name    File-Sync
%define upstream_version 0.09

Name:      perl-%{upstream_name}
Version:   %perl_convert_version %{upstream_version}
Release:   %mkrel 5

Summary:   Perl access to fsync() and sync() function calls
license:   Artistic
Group:     Development/Perl
Url:       http://search.cpan.org/dist/%{upstream_name}
Source0:   http://search.cpan.org//CPAN/authors/id/C/CE/CEVANS/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires: perl-devel
buildroot: %{_tmppath}/%{name}-%{version}-%{release}


%description
The fsync() function takes a Perl file handle as its only argument, and
passes its fileno() to the C function fsync().  It returns I<undef> on
failure, or I<true> on success.

The fsync_fd() function is used internally by fsync(); it takes a file
descriptor as its only argument.

The sync() function is identical to the C function sync().

This module does B<not> export any methods by default, but fsync() is
made available as a method of the I<FileHandle> and I<IO::Handle>
classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/man3/*
