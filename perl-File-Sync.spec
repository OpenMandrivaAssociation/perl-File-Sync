%define	module	File-Sync
%define	modver	0.11

Summary:	Perl access to fsync() and sync() function calls
Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org//CPAN/authors/id/C/CE/CEVANS/%{module}-%{modver}.tar.gz
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl-devel

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
%setup -qn %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/File
%{perl_vendorarch}/auto/File
%{_mandir}/man3/*

